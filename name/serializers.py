from rest_framework import serializers
from core import models


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = "__all__"


class PersonNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = ['id', 'name']


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profession
        fields = "__all__"
