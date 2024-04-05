from django.urls import path
from useradmin import views

urlpatterns = [
    path("", views.studio, name="studio"),
    path("video-delete/<video_id>/", views.video_delete, name="video-delete"),
]
