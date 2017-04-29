from django.db import models
from django.shortcuts import resolve_url as r
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils.crypto import get_random_string

import tagulous.models


class Ideas(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=60)
    description = models.TextField()
    likes = models.ManyToManyField(User,
                                   blank=True,
                                   related_name='ideas_likes')
    slug = models.SlugField(max_length=60, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = tagulous.models.TagField(
        blank=True,
        get_absolute_url=lambda tag: r(
            'core.views.by_tags', kwargs={'tags': tag.slug}
        ),
        max_count=5,
        force_lowercase=True,
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title + str(self.user_id)
                            + get_random_string(length=10))
        super(Ideas, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'My Idea'
        verbose_name_plural = 'My Ideas'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return r('idea_details', slug=self.slug)

    def get_api_like_url(self):
        return r('like_api', slug=self.slug)


