from django.urls import path, include
from . import views
from rest_framework import urls
from django.contrib.auth import views as authViews

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.UserViewSet)

urlpatterns = [
    path('logout/', views.UserLogoutView.as_view(), name="logout"),
    path('', include('rest_framework.urls')),
    path('', include(router.urls)),
]
