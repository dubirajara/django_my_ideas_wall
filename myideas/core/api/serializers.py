from rest_framework import serializers

from myideas.core.models import Ideas


class IdeasModelSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True, read_only=True)
    username = serializers.ReadOnlyField(source='user.username')
    likes = serializers.ReadOnlyField(source='likes.count')

    class Meta:
        model = Ideas
        fields = ('id', 'username', 'title', 'description', 'likes', 'slug', 'created_at', 'tags')
