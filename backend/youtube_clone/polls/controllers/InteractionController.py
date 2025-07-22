from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

# models
from ..models import Interaction, Comment, Video


"""
Create interaction
"""
def store_interaction(data, video):
    try:
        interaction = Interaction.objects.create(
            like = data['likes'],
            dislike = data['dislikes'],
            user_id = int(data['user'].id),
            video_id = video
        )
        
        return interaction
        
    except IntegrityError as e:
        print(f"Error creating instance due to integrity violation: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred during creation -- : {e}")
        return None
        


"""
Update interaction
"""
def update_interaction(data):
    try:
        interaction = Interaction.objects.get(id=data['interaction_id'])
        interaction.like = data['likes']
        interaction.dislike = data['dislikes']
        interaction.save()
        
        return interaction
    except ObjectDoesNotExist:
        print("Error: Interaction to update does not exist.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred during update 124 : {e}")
        return None


"""
Get Interactions by video
"""       
def get_interactionsByVideo(video_id):
    try:
        interactions = Interaction.objects.filter(video_id = video_id)
        return interactions
    except ObjectDoesNotExist:
        print("Error: Interactions not exist.")
        return None
    except Exception as e:
        print(f"An unexpected get_interaction by video: {e}")
        return None


"""
Get Interactions by video and user
"""       
def get_interactionByUserAndVideo(video, user):
    try:
        interaction = Interaction.objects.filter(video_id = video).filter(user_id = user)
        interaction = None if len(interaction) == 0 else interaction[0]
        return interaction
    except ObjectDoesNotExist:
        print("Error: Interactions not exist.")
        return None
    except Exception as e:
        print(f"An unexpected get_interaction by video and user: {e}")
        return None
    

"""
Store comment
"""
def store_comments(video_id, user, comment):
    try:
        video = Video.objects.get(pk=video_id)
        
        comment = Comment.objects.create(
            video = video,
            user = user,
            text = comment
        )
        
        return comment
    
    except IntegrityError as e:
        print(f"Error creating instance due to integrity violation: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred during creation: {e}")
        return None