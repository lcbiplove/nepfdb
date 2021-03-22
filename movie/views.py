from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from . import serializers
from auxiliary import serializers as auxSerializers
from core import models
from .permissions import IsOwner
from rest_framework.decorators import action
from django.db.models import Q
from nepfdb import paginations
from rest_framework import filters


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = models.Language.objects.all()
    serializer_class = serializers.LanguageSerializer
    permission_classes = [IsAdminUser, ]


class LanguageMovieViewset(viewsets.ModelViewSet):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieBasicSerializer

    def get_queryset(self):
        return self.queryset.filter(language=self.kwargs.get('lang_pk')).all()


class GenreViewSet(viewsets.ModelViewSet):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer
    permission_classes = [IsAdminUser, ]


class GenreMovieViewset(viewsets.ModelViewSet):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieBasicSerializer

    def get_queryset(self):
        return self.queryset.filter(genre=self.kwargs.get('genre_pk')).all()


class RatingViewSet(viewsets.ModelViewSet):
    queryset = models.Rating.objects.all()
    serializer_class = serializers.RatingSerializer
    permission_classes = [IsAdminUser, ]


class RatingMovieViewset(viewsets.ModelViewSet):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieBasicSerializer

    def get_queryset(self):
        return self.queryset.filter(rating=self.kwargs.get('rating_pk')).all()


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
    pagination_class = paginations.MediumResultsSetPagination
    filterset_fields = ['name', 'runtime']
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['name', 'runtime']


class MovieCastViewset(viewsets.ModelViewSet):
    serializer_class = serializers.CastMovieDetailSerializer
    pagination_class = paginations.LargeResultsSetPagination

    def get_queryset(self, **kwargs):
        return models.Cast.objects.filter(movie=self.kwargs.get('movie_pk')).all()


class MovieReviewViewset(viewsets.ModelViewSet):
    serializer_class = serializers.ReviewSerializer
    pagination_class = paginations.LargeResultsSetPagination

    def get_queryset(self, **kwargs):
        return models.Review.objects.filter(movie=self.kwargs.get('movie_pk')).all()


class MovieAwardCategoryViewset(viewsets.ModelViewSet):
    serializer_class = auxSerializers.AwardCategorySerializer
    pagination_class = paginations.LargeResultsSetPagination

    def get_queryset(self, **kwargs):
        return models.AwardCategory.objects.filter(
            Q(movie=self.kwargs.get('movie_pk')) |
            Q(cast__movie=self.kwargs.get('movie_pk'))
        ).all()


class MovieProductionViewset(viewsets.ModelViewSet):
    serializer_class = serializers.ProductionSerializer
    pagination_class = paginations.LargeResultsSetPagination

    def get_queryset(self, **kwargs):
        return models.Production.objects.filter(movie=self.kwargs.get('movie_pk')).all()


class ProductionViewSet(viewsets.ModelViewSet):
    queryset = models.Production.objects.all()
    serializer_class = serializers.ProductionSerializer
    pagination_class = paginations.MediumResultsSetPagination


class CastViewSet(viewsets.ModelViewSet):
    queryset = models.Cast.objects.all()
    serializer_class = serializers.CastSerializer
    pagination_class = paginations.MediumResultsSetPagination
