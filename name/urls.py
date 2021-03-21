from django.urls import path, include
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('art', views.ProfessionViewSet)
router.register('', views.PersonViewSet)

names_router = routers.NestedDefaultRouter(router, '', lookup="name")
names_router.register(
    'movies', viewset=views.PersonMovieViewset, basename="name-movie")
names_router.register(
    'awards', viewset=views.PersonAwardViewset, basename="name-award"
)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(names_router.urls)),
]
