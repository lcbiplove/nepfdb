from rest_framework import serializers
from core import models
from movie import serializers as movieSerializers
from django.utils.translation import gettext as _


class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Award
        fields = "__all__"


class AwardCategorySerializer(serializers.ModelSerializer):
    year = serializers.SerializerMethodField(read_only=True)
    award_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.AwardCategory
        fields = "__all__"
        abstract = True

    def get_year(self, obj):
        if obj.movie:
            year = obj.movie.year
        if obj.cast:
            year = obj.cast.movie.year
        return year

    def get_award_name(self, obj):
        return obj.award.name

    def validate(self, attrs):
        if (attrs.get('cast') and attrs.get('movie')) or not (attrs.get('cast') or attrs.get('movie')):
            raise serializers.ValidationError(
                _("Please select only either cast or movie."))

        return attrs


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Photo
        fields = "__all__"

    def validate(self, attrs):
        if (not attrs.get('movie') and not attrs.get('person')):
            raise serializers.ValidationError(
                _("Please select movie or person."))
        return attrs


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Photo
        fields = "__all__"


class PhotoLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Photo
        fields = ['link']
