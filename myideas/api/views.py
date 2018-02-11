from rest_framework.generics import ListAPIView, RetrieveAPIView

from myideas.core.models import Ideas

from .serializers import IdeasModelSerializer


class IdeasListApiView(ListAPIView):
    serializer_class = IdeasModelSerializer
    queryset = Ideas.objects.all()


class IdeasIdApiView(RetrieveAPIView):
    queryset = Ideas.objects.all()
    serializer_class = IdeasModelSerializer


class UserListIdApiView(ListAPIView):
    serializer_class = IdeasModelSerializer

    def get_queryset(self):
        queryset = Ideas.objects.all()
        username = self.request.query_params.get('username')
        if username is not None:
            queryset = queryset.filter(user__username=username)
            return queryset
