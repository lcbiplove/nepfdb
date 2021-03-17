from rest_framework import generics, viewsets, views
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, UserForAdminSerializer
from .permissions import IsOwnerOrAdmin


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.request.user.is_staff:
            self.serializer_class = UserForAdminSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action == "retrieve":
            self.permission_classes = [IsOwnerOrAdmin]
        return super().get_permissions()
