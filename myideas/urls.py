"""myideas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from myideas.core import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^ideas/(?P<slug>[\w-]+)/$', views.idea_details, name='idea_details'),
    url(r'^update/(?P<slug>[\w-]+)/$', views.idea_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', views.idea_delete, name='delete'),
    url(r'^api/(?P<slug>[\w-]+)/like/$', views.IdeaLikeAPI.as_view(), name='like_api'),
    url(r'^profile/(\w+)/$', views.profile, name='profile'),
    url(r'^by_tags/(?P<tags>[\w-]+)/$', views.by_tags, name='by_tags'),
    url(r'^ideas_form/', views.idea_create, name='ideas_form'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]

admin.site.site_header = 'Ideas Webapp Admin'