from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.UserViewSet)

urlpatterns = [
    path('', include('rest_framework.urls'), name="login"),
    path('', include(router.urls)),
]
