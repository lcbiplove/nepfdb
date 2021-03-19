from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.utils.translation import gettext as _

from nepfdb.utils import checkNumberAndAlpha, checkAlphaAndSpace


class UserForAdminSerializer(serializers.ModelSerializer):
    """Base Serializer for admin with all possible permissions"""
    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'name', 'password',  'is_staff']
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password", }},
        }

    def validate_name(self, value):
        if len(value.strip()) < 3 or not checkAlphaAndSpace(value):
            raise serializers.ValidationError(
                _("Name should have at least 3 alphabets only."))
        return value

    def validate_password(self, value):
        if len(value) < 6 or not checkNumberAndAlpha(value):
            raise serializers.ValidationError(
                _("Password should be greater than 6 characters with at least one number."))
        return value

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            **validated_data
        )
        login(self.context.get('request'), user)
        return user


class UserSerializer(UserForAdminSerializer):
    """Serializer without admin acces, i.e normal user serializer"""
    class Meta(UserForAdminSerializer.Meta):
        fields = ['id', 'email', 'name', 'password']


class UserIdAndNameSerializer(UserForAdminSerializer):
    """Serializer with user id and name only"""
    class Meta(UserForAdminSerializer.Meta):
        fields = ['id', 'name']
