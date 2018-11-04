from rest_framework import permissions
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .permissions import IsOwnerOrReadOnly
from .serializers import IdeasModelSerializer
from myideas.core.models import Idea


class IdeasListApiView(ListCreateAPIView):
    serializer_class = IdeasModelSerializer
    queryset = Idea.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class IdeasIdApiView(RetrieveUpdateDestroyAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeasModelSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class UserListApiView(ListAPIView):
    serializer_class = IdeasModelSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = Idea.objects.all()
        username = self.request.query_params.get('username')
        if username is not None:
            queryset = queryset.filter(user__username=username)
            return queryset
