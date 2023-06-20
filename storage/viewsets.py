from rest_framework import viewsets
from . import models
from . import serializers

class StorageViewsets(viewsets.ModelViewSet):
    queryset = models.Storage.objects.all()
    serializer_class = serializers.StorageSerializer