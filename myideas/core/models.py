from django.db import models
from django.shortcuts import resolve_url as r
from django.contrib.auth.models import User
import tagulous.models
from django.template.defaultfilters import slugify
from django.utils.crypto import get_random_string


class Ideas(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=60)
    description = models.TextField()
    slug = models.SlugField(max_length=60, blank=True, null=True)
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
        self.slug = slugify(self.title + str(self.user_id) + get_random_string(length=10))
        super(Ideas, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'My Idea'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return r('ideas_details', slug=self.slug)
