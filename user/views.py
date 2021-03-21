from rest_framework import generics, viewsets, views
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth import logout

from .serializers import UserSerializer, UserForAdminSerializer
from .permissions import IsOwnerOrAdmin
from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.request.user.is_staff:
            self.serializer_class = UserForAdminSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsOwnerOrAdmin]
        return super().get_permissions()

    def update(self, request, *args, **kwargs):
        """On update set password as hash"""
        user = self.get_object()
        password = request.data.get('password')
        user.set_password(password)
        return super().update(request, *args, **kwargs)


class UserLogoutView(views.APIView):
    def get(self, request, format=None):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request, format=None):
        logout(request)
        return Response(status=status.HTTP_200_OK)
