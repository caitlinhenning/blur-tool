import sys
import cv2
import face_recognition
from PIL import Image
import numpy as np

# Documentation: https://medium.com/@charlietapsell1989/python-pixelation-6fc490307a05

# Function to pixelate a region of an image
def pixelate_region(image, top, right, bottom, left, pixel_size):
    # Crop the region from the image
    face_image = image[top:bottom, left:right]
    # Convert the face region to a PIL Image
    face_image_pil = Image.fromarray(face_image)
    # The new dimensions based on the pixel size
    new_width = face_image_pil.width // pixel_size
    new_height = face_image_pil.height // pixel_size
    # Downsample the image to the new dimensions
    face_image_pil = face_image_pil.resize((new_width, new_height), Image.BICUBIC)
    # Upsample the image back to original dimensions
    face_image_pil = face_image_pil.resize(face_image.shape[1::-1], Image.NEAREST)
    # Convert back to a NumPy array
    return np.array(face_image_pil)

# Get the video file path from command line argument
video_file = sys.argv[1]

# Open the input video file
cap = cv2.VideoCapture(video_file)

# Get the video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, fps, (frame_width, frame_height))

# Initialize face_locations list
face_locations = []

while True:
    # Grab a single frame of video
    ret, frame = cap.read()
    
    if not ret:
        break

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)

    # Pixelate each face
    for top, right, bottom, left in face_locations:
        # Pixelate the face region
        pixelated_face = pixelate_region(rgb_frame, top, right, bottom, left, pixel_size=10)

        # Replace the original face region with the pixelated version
        frame[top:bottom, left:right] = pixelated_face[:, :, ::-1]

    # Write the frame into the output video file
    out.write(frame)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Wait for Enter key to stop
    if cv2.waitKey(25) == 13:
        break

# Release input and output video objects
cap.release()
out.release()

# Close all OpenCV windows
cv2.destroyAllWindows()