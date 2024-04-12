import cv2
import face_recognition
import sys

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

    # Draw a box around each face
    for top, right, bottom, left in face_locations:
        # Apply Gaussian blur to the face region
        face_roi = rgb_frame[top:bottom, left:right]
        blurred_face = cv2.GaussianBlur(face_roi, (51, 51), 0)

        # Draw blur over face
        cv2.rectangle(frame, (left, top), (right, bottom), (255, 255, 255), -1)
        frame[top:bottom, left:right] = blurred_face

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
