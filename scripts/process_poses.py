import cv2
import mediapipe as mp
import json
import os
import glob
import numpy as np

# Configuration
VIDEO_DIR = 'data/videos'
OUTPUT_DIR = 'data/pose_data'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Initialize MediaPipe Holistic
mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils

def process_video(video_path):
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    category = os.path.basename(os.path.dirname(video_path))
    output_path = os.path.join(OUTPUT_DIR, category, f"{video_name}.json")
    
    if os.path.exists(output_path):
        print(f"Skipping {video_name}, already processed.")
        return

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    cap = cv2.VideoCapture(video_path)
    frames_data = []
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    with mp_holistic.Holistic(
        static_image_mode=False,
        model_complexity=2,
        enable_segmentation=False,
        refine_face_landmarks=True) as holistic:
        
        frame_idx = 0
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                break
                
            # Convert BGR to RGB
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = holistic.process(image)
            
            # Extract landmarks
            frame_entry = {
                'frame': frame_idx,
                'timestamp': frame_idx / fps,
                'pose': [],
                'left_hand': [],
                'right_hand': [],
                'face': []
            }
            
            if results.pose_landmarks:
                frame_entry['pose'] = [{'x': l.x, 'y': l.y, 'z': l.z, 'visibility': l.visibility} for l in results.pose_landmarks.landmark]
                
            if results.left_hand_landmarks:
                frame_entry['left_hand'] = [{'x': l.x, 'y': l.y, 'z': l.z} for l in results.left_hand_landmarks.landmark]
                
            if results.right_hand_landmarks:
                frame_entry['right_hand'] = [{'x': l.x, 'y': l.y, 'z': l.z} for l in results.right_hand_landmarks.landmark]
                
            # Only save if we have at least hands or pose
            if frame_entry['pose'] or frame_entry['left_hand'] or frame_entry['right_hand']:
                frames_data.append(frame_entry)
                
            frame_idx += 1
            
    cap.release()
    
    # Save JSON
    with open(output_path, 'w') as f:
        json.dump({'fps': fps, 'frames': frames_data}, f)
        
    print(f"Processed {video_name}: {len(frames_data)} frames")

def main():
    video_files = glob.glob(os.path.join(VIDEO_DIR, '**/*.mp4'), recursive=True)
    print(f"Found {len(video_files)} videos to process.")
    
    for video in video_files:
        try:
            process_video(video)
        except Exception as e:
            print(f"Error processing {video}: {e}")

if __name__ == "__main__":
    main()
