from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from django.core.paginator import Paginator

# models
from ..models import Video, ViewHistory

# controllers 
from .InteractionController import get_interactionByUserAndVideo, update_interaction, store_interaction, store_comments


def store_viewHistory(video, user):
    try:
        viewHistory = ViewHistory.objects.update_or_create(
            video = video,
            user = user
        )
        return viewHistory
    except IntegrityError as e:
        print(f"Error creating instance due to integrity violation: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred during creation -- : {e}")
        return None
        

"""
Get List video randoms 
"""
def getIndex():
    list_videos = Video.objects.order_by('?')[:5]
    result = {"list_videos": list_videos}
    return result


"""
Get List video randoms 
"""
def getHistory(page_number = 1):
    histories = ViewHistory.objects.all()
    paginator = Paginator(histories, 10)
    
    page_obj = paginator.get_page(page_number)
    result = {"list_videos": page_obj}
    return result

"""
Get Detail Video
"""
def detailVideo(video_id, user):
    new_video = get_object_or_404(Video, pk = video_id)
    store_viewHistory(new_video, user) 
    interaction = get_interactionByUserAndVideo(new_video, user)
    new_video.data = interaction
    new_video.data_comments =  new_video.comments.all()
    result = {"detail": new_video} 
    return result


def set_actions_interaction(video, action, user, comment = '',):
    
    interaction = get_interactionByUserAndVideo(video, user)
    
    if interaction == None:
        data = {
            "likes": True if action == 'like' else False,
            "dislikes": True if action == 'dislike' else False,
        }
    else:
        data = {
            "likes": False if action == "dislike" else True,
            "dislikes": False if action == "like" else True,
        }
        
    
    if comment != '':
        result_comment = store_comments(video, user, comment)
        
    
    result = None
    
    if interaction == None:
        data['user'] = user
        result = store_interaction(data, video)
    elif interaction != None:
        data['interaction_id'] = interaction.id
        result = update_interaction(data)
    
    return result

"""
Apply like to video
"""
def apply_like(video_id, user):
    video = get_object_or_404(Video, pk = video_id)
    result = set_actions_interaction(video.id, 'like', user)
    return result
    
"""
Apply dislike to video
"""
def apply_dislike(video_id, user):
    video = get_object_or_404(Video, pk = video_id)
    result = set_actions_interaction(video.id, 'dislike', user)
    return result

"""
Add Comments
"""
def add_comment(video_id, comment, user):
    video = get_object_or_404(Video, pk = video_id)
    result = set_actions_interaction(video.id, 'comment', user, comment)    
    return result
    

