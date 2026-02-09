import requests
from bs4 import BeautifulSoup
import re
import os
import json
import time
from urllib.parse import urlparse

BASE_URL = 'https://diccionariolsrd.cc/diccionario/'
DATA_DIR = 'data'
VIDEOS_DIR = os.path.join(DATA_DIR, 'videos')
METADATA_FILE = os.path.join(DATA_DIR, 'dictionary.json')

# Ensure directories exist
os.makedirs(VIDEOS_DIR, exist_ok=True)

def clean_filename(text):
    """Sanitize text for use as filename"""
    text = text.lower()
    text = re.sub(r'[áàäâ]', 'a', text)
    text = re.sub(r'[éèëê]', 'e', text)
    text = re.sub(r'[íìïî]', 'i', text)
    text = re.sub(r'[óòöô]', 'o', text)
    text = re.sub(r'[úùüû]', 'u', text)
    text = re.sub(r'[ñ]', 'n', text)
    text = re.sub(r'[^a-z0-9\-_]', '-', text)
    return re.sub(r'-+', '-', text).strip('-')

def get_sign_links(soup):
    """Extract all sign links from the main page"""
    links = []
    
    # The structure seems to be category containers.
    # We'll try to find sections and their titles.
    # Based on inspection, titles might be in 'epkb-category-section__head_title'
    # and links in 'epkb-category-section__body'
    
    # Let's try to iterate over the containers if possible, or just find all title/body pairs.
    # Since the HTML structure is a bit complex, we'll try a robust approach:
    # Find all bodies, and look for the preceding title.
    
    bodies = soup.find_all('div', class_=re.compile('epkb-category-section__body'))
    
    for body in bodies:
        # Try to find category title
        # Navigate up to section container?
        section = body.find_parent('div', class_=re.compile('epkb-category-section'))
        category = "General"
        if section:
            head = section.find('div', class_=re.compile('epkb-category-section__head_title'))
            if head:
                category = head.get_text().strip()
        
        category_slug = clean_filename(category)
        
        # Get links in this body
        anchors = body.find_all('a')
        for a in anchors:
            href = a.get('href')
            title = a.get_text().strip()
            if href and title:
                links.append({
                    'category': category,
                    'category_slug': category_slug,
                    'title': title,
                    'title_slug': clean_filename(title),
                    'url': href
                })
                
    return links

def scrape_sign_page(sign_data):
    """Extract video and definition from a sign page"""
    try:
        response = requests.get(sign_data['url'], headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 1. Find Video
        video_url = None
        video_tag = soup.find('video')
        if video_tag and video_tag.get('src'):
            video_url = video_tag.get('src')
        
        # 2. Find Definition
        # Heuristic: Find text 'Interjección', 'Susantivo', 'Verbo' etc or just the first paragraph in content
        definition = ""
        # Try to find the container we identified in inspection
        # The inspection showed "eckb-article-content-..." classes.
        # Let's look for the h1 title, and take the text immediately following it.
        
        h1 = soup.find('h1', class_='eckb-article-title') 
        if not h1:
            h1 = soup.find('h1')
            
        if h1:
            # Look at siblings
            curr = h1.next_sibling
            while curr:
                if curr.name == 'p':
                    text = curr.get_text().strip()
                    if text:
                        definition = text
                        break
                curr = curr.next_sibling
                
        # Fallback: search for specific keywords in all paragraphs
        if not definition:
            keywords = ['Interjección', 'Sustantivo', 'Verbo', 'Adjetivo', 'Se usa', 'Significado']
            for p in soup.find_all('p'):
                text = p.get_text().strip()
                if any(k in text for k in keywords):
                    definition = text
                    break
        
        return {
            'video_url': video_url,
            'definition': definition
        }
        
    except Exception as e:
        print(f"Error scraping {sign_data['url']}: {e}")
        return None

def download_video(url, category_slug, filename):
    """Download video file"""
    if not url:
        return None
        
    try:
        ext = os.path.splitext(url)[1]
        if not ext: ext = '.mp4'
        
        rel_path = f"{category_slug}/{filename}{ext}"
        full_path = os.path.join(VIDEOS_DIR, rel_path)
        
        if os.path.exists(full_path):
            return rel_path # Already downloaded
            
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        # Stream download
        with requests.get(url, stream=True, timeout=30) as r:
            r.raise_for_status()
            with open(full_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
                    
        return rel_path
        
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return None

def main():
    print("Fetching dictionary index...")
    try:
        response = requests.get(BASE_URL, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.text, 'html.parser')
        links = get_sign_links(soup)
        print(f"Found {len(links)} signs.")
        
        # Load existing database if any
        database = {'signs': []}
        if os.path.exists(METADATA_FILE):
            with open(METADATA_FILE, 'r', encoding='utf-8') as f:
                try:
                    database = json.load(f)
                except: pass
                
        processed_urls = {s['original_url'] for s in database.get('signs', []) if 'original_url' in s}
        
        print(f"Already processed: {len(processed_urls)}")
        
        count = 0
        limit = 3000 # Set high for full run
        
        for sign in links:
            if sign['url'] in processed_urls:
                continue
                
            if count >= limit:
                print(f"Reached limit of {limit} for this run.")
                break
                
            print(f"Processing [{count+1}/{limit}] {sign['title']} ({sign['category']})...")
            
            details = scrape_sign_page(sign)
            if details:
                # Download video
                local_video = download_video(
                    details['video_url'], 
                    sign['category_slug'], 
                    sign['title_slug']
                )
                
                entry = {
                    'id': sign['title_slug'],
                    'word': sign['title'],
                    'category': sign['category'],
                    'definition': details['definition'],
                    'video_file': local_video,
                    'video_url': details['video_url'],
                    'original_url': sign['url']
                }
                
                database['signs'].append(entry)
                
                # Save periodically
                if count % 5 == 0:
                    with open(METADATA_FILE, 'w', encoding='utf-8') as f:
                        json.dump(database, f, indent=2, ensure_ascii=False)
                        
            count += 1
            time.sleep(0.5) # Polite delay
            
        # Final save
        with open(METADATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(database, f, indent=2, ensure_ascii=False)
            
        print("Done!")
        
    except Exception as e:
        print(f"Fatal error: {e}")

if __name__ == "__main__":
    main()
