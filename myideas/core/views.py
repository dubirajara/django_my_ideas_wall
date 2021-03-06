from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from rest_framework.views import APIView
from rest_framework import authentication, permissions

from registration.forms import User

from .models import Idea
from .forms import IdeasForm
from .mixins import LikeIdeasMixin


def home(request):
    queryset = Idea.objects.all()
    context = {
        'ideas': queryset,
    }

    return render(request, 'index.html', context)


def idea_details(request, slug):
    ideas = get_object_or_404(Idea, slug=slug)

    context = {
        'ideas': ideas,
    }

    return render(request, 'ideas_details.html', context)


@login_required
def idea_create(request):
    form = IdeasForm(request.POST)
    if form.is_valid():
        idea = form.save(commit=False)
        idea.user = request.user
        idea.save()
        form.save_m2m()
        return HttpResponseRedirect('/')

    else:
        form = IdeasForm()

    context = {
        'form': form,
        'form_media': form.media,
    }

    return render(request, 'idea_form.html', context)


@login_required
def idea_update(request, slug=None):
    instance = get_object_or_404(Idea, slug=slug)
    form = IdeasForm(request.POST or None, instance=instance)
    if request.user == instance.user:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(instance.get_absolute_url())

        context = {
            'form': form,
        }
    else:
        raise PermissionDenied

    return render(request, 'update.html', context)


@login_required
def idea_delete(request, slug=None):
    instance = get_object_or_404(Idea, slug=slug)
    if request.user == instance.user:
        instance.delete()
        return HttpResponseRedirect(reverse(
            'profile', args=(request.user.username,)
        ))
    else:
        raise PermissionDenied


def by_tags(request, tags):
    queryset = Idea.objects.filter(tags=tags)

    context = {
        'queryset': queryset
    }

    return render(request, 'by_tags.html', context)


def profile(request, username):
    user = get_object_or_404(User.objects, username=username)
    queryset = Idea.objects.filter(user=user)

    context = {
        'username': user,
        'ideas': queryset,
    }
    return render(request, 'profile.html', context)


# thanks the snippet video tutorial django likes: https://www.youtube.com/watch?v=pkPRtQf6oQ8
class IdeaLikeAPI(LikeIdeasMixin, APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)


# by_tags = TagsIdeasMixin.as_view()
