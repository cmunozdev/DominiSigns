import requests
from bs4 import BeautifulSoup
import re

url = 'https://diccionariolsrd.cc/diccionario/'
try:
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.text, 'html.parser')
    
    print(f"Title: {soup.title.string}")
    
    # Extract links from category sections
    category_sections = soup.find_all('div', class_=re.compile('epkb-category-section'))
    print(f"\nFound {len(category_sections)} category sections.")
    
    all_links = []
    for section in category_sections:
        # Get category title if available
        title_div = section.find('div', class_=re.compile('epkb-category-section__head_title'))
        cat_title = title_div.get_text().strip() if title_div else "Unknown"
        
        # Get links
        links = section.find_all('a')
        print(f"Category '{cat_title}': {len(links)} links found.")
        for l in links:
            all_links.append((cat_title, l.get('href'), l.get_text().strip()))

    print(f"\nTotal unique links found: {len(all_links)}")
    for i, (cat, href, text) in enumerate(all_links[:10]):
         print(f"{i+1}. [{cat}] {text} -> {href}")

except Exception as e:
    print(f"Error: {e}")
