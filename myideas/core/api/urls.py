"""tweetme URL Configuration

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
from django.conf.urls import url

from tweetme.tweets.api import views

urlpatterns = [
    url(r'^$', views.TweetListApiView.as_view(), name='list'),
    # url(r'^(?P<pk>\d+)/$', views.TweetDetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>\d+)/update/$', views.TweetUpdateView.as_view(), name='update'),
    # url(r'^(?P<pk>\d+)/delete/$', views.TweetDeleteView.as_view(), name='delete'),
    # url(r'^create/$', views.TweetCreateView.as_view(), name='create')
]
