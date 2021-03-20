from rest_framework import serializers
from core import models


class PersonSerializer(serializers.ModelSerializer):
    awards = serializers.SerializerMethodField(read_only=True)
    photos = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Person
        fields = "__all__"

    def get_awards(self, obj):
        award = models.AwardCategory.objects.filter(
            cast__in=obj.cast_set.all()).all() or None

        if award:
            award = {
                "wins": award.filter(isWinner=True).count(),
                "nominations": award.count(),
            }
        return award

    def get_photos(self, obj):
        queryset = obj.photo_set.all()
        return [x.link for x in queryset]


class PersonNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = ['id', 'name']


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profession
        fields = "__all__"
