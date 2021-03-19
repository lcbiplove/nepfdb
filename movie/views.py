from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from . import serializers
from core import models
from .permissions import IsOwner


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


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = [IsAuthenticated, ]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        if self.action == "create":
            context['create'] = True
        return context


class MovieViewSet(viewsets.ModelViewSet):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    # permission_classes = [IsAdminUser, ]


class ProductionViewSet(viewsets.ModelViewSet):
    queryset = models.Production.objects.all()
    serializer_class = serializers.ProductionSerializer


class CastViewSet(viewsets.ModelViewSet):
    queryset = models.Cast.objects.all()
    serializer_class = serializers.CastSerializer
