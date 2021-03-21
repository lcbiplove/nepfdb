from django.urls import path, include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('awards', viewset=views.AwardViewSet)
router.register('award-categories', viewset=views.AwardCategoryViewSet)
router.register('images', viewset=views.PhotoViewSet)

award_router = routers.NestedDefaultRouter(router, 'awards', lookup="award")
award_router.register(
    'categories', viewset=views.AwardAwardCategoryViewset, basename="award-award-category")

urlpatterns = [
    path('', include(router.urls)),
    path('', include(award_router.urls)),
]
