from rest_framework import viewsets
from rest_framework.response import Response
from core import models
from . import serializers
from movie import serializers as movieSerializers
from auxiliary import serializers as auxSerializers
from django.db.models import Q


class PersonViewSet(viewsets.ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer


class ProfessionViewSet(viewsets.ModelViewSet):
    queryset = models.Profession.objects.all()
    serializer_class = serializers.ProfessionSerializer


class PersonMovieViewset(viewsets.ModelViewSet):
    queryset = models.Movie.objects.all()
    serializer_class = movieSerializers.MovieBasicSerializer

    def get_queryset(self):
        return self.queryset.distinct().filter(
            Q(cast__person=self.kwargs.get('name_pk')) |
            Q(production__person=self.kwargs.get('name_pk'))
        ).all()


class PersonAwardViewset(viewsets.ModelViewSet):
    queryset = models.AwardCategory.objects.all()
    serializer_class = auxSerializers.AwardCategorySerializer

    def get_queryset(self):
        return self.queryset.filter(cast__person=self.kwargs.get('name_pk'))
