from rest_framework import viewsets
from core.models import Obras
from core.serializer import CoreSerializer


class CoreViewSet(viewsets.ModelViewSet):
    queryset = Obras.objects.all()
    serializer_class = CoreSerializer
