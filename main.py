import numpy as np
import cv2

from utils import find_faces, take_photo

# your folder default to store pictures
# FACE_FOLDER = 'audrey'
FACE_FOLDER = False

# Get webcam source
cam = cv2.VideoCapture(0)

while cam.isOpened():
    # Get a frame (the function recovers whether or not there was an error in loading the frame)
    error, frame = cam.read()

    # If you want a good result
    image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Convert the frame to an array
    image = np.array(frame)

    # Face recognition press key R
    if cv2.waitKey(1) & 0xFF == ord('r'):
        print("Processing")
        result = find_faces(image)
        print(f"Hello, {result}!")
        continue

    # Take a picture press key P
    if cv2.waitKey(1) & 0xFF == ord('p'):
        print("Wait...")
        _, result = take_photo(image, FACE_FOLDER)
        print(result)
        continue

    # Quit the webcam with key Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Show the frame loaded
    cv2.imshow('Video', image)

cam.release()
