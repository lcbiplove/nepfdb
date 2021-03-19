from rest_framework import viewsets
from rest_framework.response import Response
from core import models
from . import serializers


class PersonViewSet(viewsets.ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer


class ProfessionViewSet(viewsets.ModelViewSet):
    queryset = models.Profession.objects.all()
    serializer_class = serializers.ProfessionSerializer
