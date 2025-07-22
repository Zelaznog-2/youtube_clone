import datetime
import uuid
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

## Custom user
# class CustomUser(AbstractUser):
#     is_active = models.BooleanField(default=False)
    
#     class Meta:
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'

#     def __str__(self):
#         return self.username

## Model video
class Video(models.Model):
    url_embed = models.URLField(max_length=500)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='videos_uploaded'
    )
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
    
    def __str__(self):
        return self.title
    
    @property
    def total_likes(self):
        return self.interactions.filter(like=True).count()
    
    @property
    def total_dislikes(self):
        return self.interactions.filter(dislike=True).count()
    
    @property
    def total_comments(self):
        return self.comments.count()
    
    @property
    def popularity_score(self):
        days_since_upload = (timezone.now() - self.created_at).days
        recency_bonus = max(0, 100 - (days_since_upload * 100))
        
        return (
            (self.total_likes * 10) - 
            (self.total_dislikes * 5) + 
            self.total_comments + 
            recency_bonus
        )
    
    def was_published_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)

## Model Interaction
class Interaction(models.Model):
    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
        related_name='interactions'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_interactions'
    )
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('video', 'user')  # Un usuario solo puede interactuar una vez por video
        verbose_name = 'Interaction'
        verbose_name_plural = 'Interactions'
    
    def __str__(self):
        return f"{self.user.username} - {self.video.title}"
    
    def save(self, *args, **kwargs):
        # Evitamos que los dos no están activos al mismo tiempo
        if self.like and self.dislike:
            self.dislike = False
        super().save(*args, **kwargs)

## Model Comments
class Comment(models.Model):
    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_comments'
    )
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
    
    def __str__(self):
        return f"{self.user.username} - {self.text[:50]}"
    


## Model Historial
class ViewHistory(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='view_history'
    )
    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
        related_name='views_history'
    )
    viewed_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-viewed_at']
        verbose_name = 'History Visualization'
        verbose_name_plural = 'History Visualizations'
    
    def __str__(self):
        return f"{self.user.username} vio {self.video.title}"
