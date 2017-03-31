from django.conf.urls import url

from myideas.core import views

urlpatterns = [

    url(r'^ideas_form/', views.idea_create, name='ideas_form'),
    url(r'^(?P<slug>[\w-]+)/$', views.idea_details, name='idea_details'),
    url(r'^update/(?P<slug>[\w-]+)/$', views.idea_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', views.idea_delete, name='delete'),
    url(r'^api/(?P<slug>[\w-]+)/like/$', views.IdeaLikeAPI.as_view(), name='like_api'),
    url(r'^profile/(\w+)/$', views.profile, name='profile'),
    url(r'^by_tags/(?P<tags>[\w-]+)/$', views.by_tags, name='by_tags'),
]