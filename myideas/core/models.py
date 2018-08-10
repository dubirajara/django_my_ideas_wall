from django.db import models
from django.shortcuts import resolve_url as r
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


import tagulous.models


class Idea(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Idea.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super(Idea, self).save(*args, **kwargs)

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
