from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserListView.as_view()),
    path('register/', views.UserRegisterView.as_view()),
    path('register/admin/', views.UserRegisterByAdminView.as_view()),
]
