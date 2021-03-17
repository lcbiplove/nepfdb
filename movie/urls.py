from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('', viewset=views.MovieViewSet)
router.register('lang', viewset=views.LanguageViewSet)
router.register('genre', viewset=views.GenreViewSet)
router.register('rating', viewset=views.RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
