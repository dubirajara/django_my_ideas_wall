from django.contrib import admin
import tagulous.admin
from .models import Ideas


class IdeasAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('title',)}
    list_display = ('user', 'title', 'likes', 'created_at', 'tags')
    list_display_links = ('title',)
    exclude = ('likes',)
    model = Ideas


tagulous.admin.register(Ideas, IdeasAdmin)
tagulous.admin.register(Ideas.tags.tag_model)
