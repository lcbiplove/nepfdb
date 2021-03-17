from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from . import serializers
from core import models


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = models.Language.objects.all()
    serializer_class = serializers.LanguageSerializer
    permission_classes = [IsAdminUser, ]


class GenreViewSet(viewsets.ModelViewSet):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer
    permission_classes = [IsAdminUser, ]


class RatingViewSet(viewsets.ModelViewSet):
    queryset = models.Rating.objects.all()
    serializer_class = serializers.RatingSerializer
    permission_classes = [IsAdminUser, ]


class MovieViewSet(viewsets.ModelViewSet):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    # permission_classes = [IsAdminUser, ]
