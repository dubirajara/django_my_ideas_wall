from rest_framework.generics import ListAPIView, RetrieveAPIView

from myideas.core.models import Ideas

from .serializers import IdeasModelSerializer


class IdeasListApiView(ListAPIView):
    serializer_class = IdeasModelSerializer
    queryset = Ideas.objects.all()


class IdeasIdApiView(RetrieveAPIView):
    queryset = Ideas.objects.all()
    serializer_class = IdeasModelSerializer


