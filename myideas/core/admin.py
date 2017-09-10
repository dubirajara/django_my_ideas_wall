from django.contrib import admin
import tagulous.admin
from .models import Ideas


class IdeasAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'created_at', 'tags')
    list_display_links = ('title',)
    model = Ideas


tagulous.admin.register(Ideas, IdeasAdmin)
tagulous.admin.register(Ideas.tags.tag_model)
