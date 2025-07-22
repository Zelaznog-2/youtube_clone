from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

# Controller 
from .controllers.VideosController import getIndex, detailVideo, apply_like, apply_dislike, add_comment, getHistory
from .controllers.AuthController import set_authenticate, set_register
# Create your views here.

# View Index
@require_http_methods(['GET'])
def index(request):
    result = getIndex()
    return render(request, "polls/index.html", result)


@require_http_methods(['GET'])
def histories(request):
    page_number = request.GET.get("page")
    result = getHistory(page_number)
    return render(request, "polls/videos/histories.html", result)

# View Detail
@require_http_methods(['GET'])
def detail(request, video_id):
    user = request.user
    print('user_id', user)
    result = detailVideo(video_id, user)
    return render(request, "polls/videos/detail.html", result)

# Action Interaction Like
@login_required
@require_http_methods(['GET'])
def like(request, video_id):
    user = request.user
    apply_like(video_id, user)
    return redirect(reverse('detail', args=[video_id]))

# Action Interaction Dislike
@login_required
@require_http_methods(['GET'])
def dislike(request, video_id):
    user = request.user
    apply_dislike(video_id, user)
    return redirect(reverse('detail', args=[video_id]))

# Action Interaction Comments
@require_http_methods(['POST'])
def comments(request, video_id):
    user = request.user
    comment = request.POST['comment']
    add_comment(video_id, comment, user)
    return redirect(reverse('detail', args=[video_id]))


# Action Login
@require_http_methods(['POST'])
def modal_login(request):
    result = set_authenticate(request)
    print('prueba', result)
    return redirect('index')
    
# Action Register
@require_http_methods(['POST'])
def modal_register(request):
    set_register(request)
    return redirect(request.path)

