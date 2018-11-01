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
from django.urls import path, include
from django.contrib import admin
from myideas.core import views

urlpatterns = [
    path('ideas/', include('myideas.core.urls')),
    path('api/v1/', include('myideas.api.urls')),
    path('ideassecretadmin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('registration.backends.default.urls')),
    path('oauth', include('social_django.urls', namespace='social')),
]

admin.site.site_header = 'Ideas Webapp Admin'
