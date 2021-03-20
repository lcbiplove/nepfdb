from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('awards', viewset=views.AwardViewSet)
router.register('award-category', viewset=views.AwardCategoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]
