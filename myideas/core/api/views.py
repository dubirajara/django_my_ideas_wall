from rest_framework.generics import ListAPIView

from myideas.core.models import Ideas
from .serializers import IdeasModelSerializer


class IdeasListApiView(ListAPIView):
    serializer_class = IdeasModelSerializer
    queryset = Ideas.objects.all()
