from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import login


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'name', 'is_staff']


class UserRegisertByAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'name', 'password',  'is_staff']
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password", }},
        }

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            **validated_data
        )
        login(self.context.get('request'), user)
        return user


class UserRegisterSerializer(UserRegisertByAdminSerializer):
    class Meta(UserRegisertByAdminSerializer.Meta):
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password", }},
            "is_staff": {"read_only": True},
        }
