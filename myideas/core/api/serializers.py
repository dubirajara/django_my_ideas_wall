from rest_framework import serializers

from tweetme.accounts.api.serializers import UserDisplaySerializer
from tweetme.tweets.models import Tweet


class TweetModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer()

    class Meta:
        model = Tweet
        fields = ('user', 'content')
