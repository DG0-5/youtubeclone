from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from core.models import Comment, Video
from channel.models import Channel
from django.db.models import Count, Q
from django.views.decorators.csrf import csrf_exempt
from taggit.models import Tag

# Create your views here.
def index(request):
    video = Video.objects.filter(visibility='public').order_by("-date")
    context = {
        'video': video,
    }
    return render(request, 'index.html', context)

def videoDetail(request, pk):
    video = Video.objects.get(id=pk)
    channel = Channel.objects.get(user=video.user)
    
    channel.total_views += 1
    channel.save()
    
    video.views = video.views + 1
    video.save()
    
    video_tags_id = video.tags.values_list('id', flat=True)
    similar_videos = Video.objects.filter(tags__in=video_tags_id).exclude(id=video.id)
    similar_videos = similar_videos.annotate(same_tags=Count('tags')).order_by('-same_tags','-date')[:25]
    
    comment = Comment.objects.filter(active=True, video=video).order_by('-date')
    
    context = {
        'video': video,
        'comment': comment,
        'similar_videos': similar_videos,
        'channel': channel,
        
    }
    return render(request, 'video-detail.html', context)

def save_video(request, video_id):
    video = Video.objects.get(id=video_id)
    user = request.user.profile
    
    if video in user.saved_videos.all():
        user.saved_videos.remove(video)
    else:
        user.saved_videos.add(video)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

def ajax_save_comment(request):
    if request.method == "POST":
        pk = request.POST.get("id")
        comment = request.POST.get("comment")
        video = Video.objects.get(id=pk)
        user = request.user
        
        new_comment = Comment.objects.create(comment=comment, user=user, video=video)
        new_comment.save()
        
        response = "Comment Posted"
        return HttpResponse(response)

@csrf_exempt
def ajax_delete_comment(request):
    if request.method == "POST":
        id = request.POST.get('cid')
        comment = Comment.objects.get(id=id)
        comment.delete()
        return JsonResponse({"status": 1})
    else:
        return JsonResponse({"status": 2})
    
# Add Subscribers
def add_new_subscribers(request, id):
    subs = Channel.objects.get(id=id)
    user = request.user
    if user in subs.subscribers.all():
        subs.subscribers.remove(user)
        response = "Subscribe"
        return JsonResponse(response, safe=False, status=200)
    else:
        subs.subscribers.add(user)
        response = "UnSubscribe"
        return JsonResponse(response, safe=False, status=200)
    
# Load Subscribers
def load_new_subscribers(request, id):
    subscribers = Channel.objects.get(id=id)
    sub_lists = list(subscribers.subscribers.values())
    return JsonResponse(sub_lists, safe=False, status=200)

# Add Likes
def add_new_like(request, id):
    video = Video.objects.get(id=id)
    user = request.user
    if user in video.likes.all():
        video.likes.remove(user)
        like_response = '<i class="fa fa-thumbs-up"></i>'
        return JsonResponse(like_response, safe=False, status=200)
    else:
        video.likes.add(user)
        like_response = '<i class="fa fa-thumbs-up"></i>'
        return JsonResponse(like_response, safe=False, status=200)
    
# Load Likes
def load_video_likes(request, id):
    likes = Video.objects.get(id=id)
    likes_lists = list(likes.likes.values())
    return JsonResponse(likes_lists, safe=False, status=200)

def search_view(request):
    video = Video.objects.filter(visibility="public").order_by("-date")
    query = request.GET.get("q")
    if query:
        video = video.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        ).distinct()
    
    context = {
        'video': video,
        'query': query,
    }
    return render(request, 'search.html', context)

def tag_list(request, tag_slug=None):
    video = Video.objects.filter(visibility="public").order_by("-date")
    tag = None
    
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        video = video.filter(tags__in=[tag])
    
    context = {
        'video': video,
        'tag': tag,
    }
    return render(request, 'tags.html', context)


def trending(request):
    video = Video.objects.filter(visibility="public").order_by("-views")
    context = {
        "video":video
    }
    return render(request, "trending.html", context)
    

def savedVideos(request):
    try:
        video = request.user.profile.saved_videos.all()
    except:
        video = None
    context = {
        "video":video
    }
    return render(request, "saved-video.html", context)
    

