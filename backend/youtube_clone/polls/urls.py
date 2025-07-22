from django.urls import path

from . import views

urlpatterns = [
    # Videos
    path("", views.index, name="index"),
    path("detail/<int:video_id>", views.detail, name="detail"),
    # Videos Interactions
    path("interaction/<int:video_id>/like", views.like, name="like"),
    path("interaction/<int:video_id>/dislike", views.dislike, name="dislike"),
    path("interaction/<int:video_id>/comment", views.comments, name="comments"),
    # Auth 
    path('auth/login', views.modal_login, name="login"),
    path('auth/register', views.modal_register, name="register"),
    # Histories
    path('histories', views.histories, name="histories")
]