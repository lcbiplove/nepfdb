from rest_framework import viewsets
from . import serializers
from core import models


class AwardViewSet(viewsets.ModelViewSet):
    queryset = models.Award.objects.all()
    serializer_class = serializers.AwardSerializer


class AwardCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.AwardCategory.objects.all()
    serializer_class = serializers.AwardCategorySerializer
