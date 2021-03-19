from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('art', views.ProfessionViewSet)
router.register('', views.PersonViewSet)

urlpatterns = [
    path('', include(router.urls))
]
