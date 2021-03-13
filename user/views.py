from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, UserRegisertByAdminSerializer, UserRegisterSerializer


class UserListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserRegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserRegisterSerializer


class UserRegisterByAdminView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserRegisertByAdminSerializer
