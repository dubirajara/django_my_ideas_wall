from django.urls import path

from myideas.core import views

urlpatterns = [

    path('ideas_form/', views.idea_create, name='ideas_form'),
    path('<slug:slug>/', views.idea_details, name='idea_details'),
    path('update/<slug:slug>/', views.idea_update, name='update'),
    path('<slug:slug>/delete/', views.idea_delete, name='delete'),
    path('api/<slug:slug>/like/', views.IdeaLikeAPI.as_view(), name='like_api'),
    path('profile/<username>/', views.profile, name='profile'),
    path('by_tags/<tags>/', views.by_tags, name='by_tags'),
]