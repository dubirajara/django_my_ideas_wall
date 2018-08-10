from django.contrib import admin
import tagulous.admin
from .models import Idea


class IdeasAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'created_at', 'tags')
    list_display_links = ('title',)
    model = Idea


tagulous.admin.register(Idea, IdeasAdmin)
tagulous.admin.register(Idea.tags.tag_model)
