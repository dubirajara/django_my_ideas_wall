from rest_framework import serializers

from myideas.core.models import Ideas


class IdeasModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ideas
        fields = ('user', 'title', 'description', 'likes', 'slug', 'tags', 'created_at')
