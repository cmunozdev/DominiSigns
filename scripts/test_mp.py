import mediapipe as mp
try:
    print(f"MediaPipe version: {mp.__version__}")
    print(f"Solutions: {dir(mp.solutions)}")
    mp_holistic = mp.solutions.holistic
    print("Holistic module found")
    with mp_holistic.Holistic() as holistic:
        print("Holistic object created successfully")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
