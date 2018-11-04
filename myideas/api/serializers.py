from rest_framework import serializers

from myideas.core.models import Idea


class IdeasModelSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="id_api")
    tags = serializers.StringRelatedField(many=True, read_only=True)
    username = serializers.ReadOnlyField(source='user.username')
    likes = serializers.ReadOnlyField(source='likes.count')
    user = serializers.ReadOnlyField(source='user.user')

    class Meta:
        model = Idea
        fields = ('url', 'id', 'username', 'title', 'description', 'likes', 'slug', 'created_at', 'tags', 'user')
