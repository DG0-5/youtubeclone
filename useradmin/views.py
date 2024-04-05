from django.shortcuts import render
from channel.models import Channel
from core.models import Video
from django.contrib.auth.decorators import login_required

@login_required
def studio(request):
    user = request.user
    channel = user.channel
    
    channel = Channel.objects.get(user=user)
    video = Video.objects.filter(user=user)
    
    context = {
        "user": user,
        "channel": channel,
        "video": video,
    }
    
    return render(request, 'useradmin/studio.html', context)

def video_delete(request, video_id):
    user = request.user
    video = Video.objects.get(id=video_id, user=user)
    video.delete()