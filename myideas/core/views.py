from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from registration.forms import User
from .forms import IdeasForm, IdeasFormUpdate
from .models import Ideas


def home(request):
    queryset = Ideas.objects.all()
    context = {
        'ideas': queryset,
    }

    return render(request, 'index.html', context)


def idea_details(request, slug):
    ideas = get_object_or_404(Ideas, slug=slug)

    context = {
        'ideas': ideas,
    }

    return render(request, 'ideas_details.html', context)


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


def idea_update(request, slug=None):
    instance = get_object_or_404(Ideas, slug=slug)
    form = IdeasFormUpdate(request.POST or None, instance=instance)
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


def idea_delete(request, slug=None):
    instance = get_object_or_404(Ideas, slug=slug)
    if request.user == instance.user:
        instance.delete()
        return HttpResponseRedirect(reverse(
            'profile', args=(request.user.username,)
        ))
    else:
        raise PermissionDenied


def by_tags(request, tags):
    queryset = Ideas.objects.filter(tags=tags)

    context = {
        'queryset': queryset
    }

    return render(request, 'by_tags.html', context)


def profile(request, username):
    user = get_object_or_404(User.objects, username=username)
    queryset = Ideas.objects.filter(user=user)

    context = {
        'username': user,
        'ideas': queryset,
    }

    return render(request, 'profile.html', context)
