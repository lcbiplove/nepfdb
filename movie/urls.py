from django.urls import path, include
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('lang', viewset=views.LanguageViewSet)
router.register('genre', viewset=views.GenreViewSet)
router.register('rating', viewset=views.RatingViewSet)
router.register('review', viewset=views.ReviewViewSet)
router.register('prod', viewset=views.ProductionViewSet)
router.register('cast', viewset=views.CastViewSet)
router.register('', viewset=views.MovieViewSet)

movies_router = routers.NestedDefaultRouter(router, '', lookup="movie")
movies_router.register(
    'casts', viewset=views.MovieCastViewset, basename='movie-cast')
movies_router.register(
    'reviews', viewset=views.MovieReviewViewset, basename='movie-review')
movies_router.register(
    'awards', viewset=views.MovieAwardCategoryViewset, basename='movie-award')
movies_router.register(
    'prod', viewset=views.MovieProductionViewset, basename='movie-prod')

lang_router = routers.NestedDefaultRouter(router, 'lang', lookup="lang")
lang_router.register(
    'movies', viewset=views.LanguageMovieViewset, basename='lang-movie')

genre_router = routers.NestedDefaultRouter(router, 'genre', lookup="genre")
genre_router.register(
    'movies', viewset=views.GenreMovieViewset, basename='genre-movie')

rating_router = routers.NestedDefaultRouter(router, 'rating', lookup="rating")
rating_router.register(
    'movies', viewset=views.RatingMovieViewset, basename='rating-movie')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(movies_router.urls)),
    path('', include(lang_router.urls)),
    path('', include(genre_router.urls)),
    path('', include(rating_router.urls)),
]
