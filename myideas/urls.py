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
from django.conf import settings
from django.conf.urls.static import static
from myideas.core import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^ideas/(?P<slug>[\w-]+)/$', views.idea_details, name='idea_details'),
    url(r'^update/(?P<slug>[\w-]+)/$', views.idea_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', views.idea_delete, name='delete'),
    url(r'^profile/(\w+)/$', views.profile, name='profile'),
    url(r'^by_tags/(?P<tags>[\w-]+)/$', views.by_tags, name='by_tags'),
    url(r'^ideas_form/', views.idea_create, name='ideas_form'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^oauth/', include('social.apps.django_app.urls', namespace='social')),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Ideas Webapp Admin'