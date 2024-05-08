from django.shortcuts import render
from .models import CrowdDensity
from .utils import detect_faces, count_people


def crowd_detection_view(request):
    # latest_density = CrowdDensity.objects.order_by("-timestamp").first()
    # context = {"latest_density": latest_density}
    image_path = CrowdDensity.objects.order_by("-timestamp").first()

    # Detect faces in the image
    faces = detect_faces(image_path)

    # Count the number of people (faces) detected
    num_people = len(faces)

    # Set a threshold for overcrowding
    max_limit = 2  # Define your maximum crowd limit here

    # Check if the crowd exceeds the threshold
    if num_people > max_limit:
        overcrowded = True
        print("overcrowded")
    else:
        overcrowded = False
        print("everything is ok")

    # Render the template with context
    context = {
        "num_people": num_people,
        "overcrowded": overcrowded,
    }
    return render(request, "crowd/crowd_detection.html", context)
