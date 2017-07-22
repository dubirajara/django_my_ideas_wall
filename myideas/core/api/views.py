from rest_framework import generics

from myideas.core.models import Ideas
from .serializers import IdeasModelSerializer


class IdeasListApiView(generics.ListAPIView):
    serializer_class = IdeasModelSerializer

    def get_queryset(self):
        return Ideas.objects.all()