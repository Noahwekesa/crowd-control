from django.shortcuts import render
from .utils import detect_faces
import cv2
import base64
from . import send_sms


def crowd_detection_view(request):
    # Initialize video capture from webcam
    cap = cv2.VideoCapture(0)  # 0 for default webcam, change if necessary

    if not cap.isOpened():
        # Handle case where camera is not available
        return render(request, "crowd/camera_unavailable.html")

    # Set a threshold for overcrowding
    max_limit = 1  # Define your maximum crowd limit here

    while cap.isOpened():
        # Capture frame-by-frame
        success_frame, frame = cap.read()

        if success_frame:
            # Detect faces in the frame
            faces = detect_faces(frame)

            # Count the number of people (faces) detected
            num_people = len(faces)

            # Check if the crowd exceeds the threshold
            overcrowded = num_people > max_limit
            if overcrowded:
                send_sms.SMS().send()
            # Convert the frame to JPEG format
            _, jpeg_frame = cv2.imencode(".jpg", frame)

            # Encode the frame in base64 format
            base64_frame = base64.b64encode(jpeg_frame).decode("utf-8")

            # Render the template with context
            context = {
                "num_people": num_people,
                "overcrowded": overcrowded,
                "base64_frame": base64_frame,  # Pass the base64 encoded frame to the template
            }

            # Release the video capture
            cap.release()

            return render(request, "crowd/crowd_detection.html", context)
        else:
            # Handle case where frame could not be read
            return render(request, "crowd/frame_unavailable.html")

    # Release the video capture (in case the loop is exited without returning)
    cap.release()

    # Return a default response if the loop exits without returning
    return render(request, "crowd/default_response.html")
