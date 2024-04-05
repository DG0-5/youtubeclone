from django.urls import path
from channel import views

urlpatterns = [
    path("<channel_name>/", views.channel_profile, name='channel-profile'),
    path("<channel_name>/videos/", views.channel_videos, name='channel-video'),
    path("<channel_name>/about/", views.channel_about, name='channel-about'),
    path("<channel_name>/community/", views.channel_community, name='channel-community'),
    path("<channel_name>/community/<int:community_id>/", views.community_detail, name='community-detail'),
    
    # Comment Section
    
    # Create Comment
    path("community/<int:community_id>/create-comment/", views.create_community_comment, name='create-community-comment'),
    
    # Delete Comment
    path("community/<int:community_id>/<int:comment_id>/", views.delete_community_comment, name='delete-community-comment'),
    
    # Like Comment
    path("community/<int:community_id>/like/", views.like_community_post, name='like-community-post'),
    
    # Uploading Video
    path("channel/create/video/", views.video_upload, name='upload-video'),
    
    # Editing Video
    path("channel/edit-video/<channel_id>/<video_id>", views.video_edit, name='video-edit'),
    
    # Create Community Post
    path("channel/create-community-post/<channel_id>/", views.create_community_post, name='create-post'),
    
    # Edit Community Post
    path("channel/edit-community-post/<channel_id>/<community_post_id>", views.edit_community_post, name='edit-post'),
    
    # Delete Community Post
    path("channel/delete-community-post/<channel_id>/<post_id>", views.delete_community_post, name='delete-post'),
]
