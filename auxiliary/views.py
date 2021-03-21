from rest_framework import viewsets
from . import serializers
from core import models


class AwardViewSet(viewsets.ModelViewSet):
    queryset = models.Award.objects.all()
    serializer_class = serializers.AwardSerializer


class AwardCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.AwardCategory.objects.all()
    serializer_class = serializers.AwardCategorySerializer


class AwardAwardCategoryViewset(viewsets.ModelViewSet):
    queryset = models.AwardCategory.objects.all()
    serializer_class = serializers.AwardCategorySerializer

    def get_queryset(self):
        return self.queryset.filter(award=self.kwargs.get('award_pk'))


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = models.Photo.objects.all()
    serializer_class = serializers.PhotoSerializer
