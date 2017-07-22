from rest_framework import generics

from tweetme.tweets.models import Tweet
from .serializers import TweetModelSerializer


class TweetListApiView(generics.ListAPIView):
    serializer_class = TweetModelSerializer

    def get_queryset(self):
        return Tweet.objects.all()