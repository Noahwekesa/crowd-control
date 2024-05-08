from django.urls import path
from . import views

urlpatterns = [
    path("", views.crowd_detection_view),
]
