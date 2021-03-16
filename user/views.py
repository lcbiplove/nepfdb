from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, UserForAdminSerializer
from .permissions import IsOwnerOrAdmin


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrAdmin]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        """If user is admin, give all features"""
        if self.request.user.is_staff:
            self.serializer_class = UserForAdminSerializer
        return super().get_serializer_class()
