from rest_framework import serializers
from core import models
from django.utils.translation import gettext as _
from django.db.models import Avg
from name import serializers as nameSerializer
from user import serializers as userSerializer


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Language
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rating
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'
        extra_kwargs = {
            "reviewer": {"read_only": True, },
        }

    def validate_vote(self, value):
        if value < 1 or value > 10:
            raise serializers.ValidationError(
                _("Please enter number from 1 to 10."))

        # round off to nearest .5 or .0 posititon
        value = 0.5 * round(float(value)/0.5)
        return value

    def validate(self, attrs):
        reviewer = self.context.get('request').user
        if self.context.get('create'):
            movie = attrs.get('movie')
            exists = models.Review.objects.filter(
                movie__id=movie.id, reviewer__id=reviewer.id).exists()

            if exists:
                raise serializers.ValidationError(
                    _("You have already added a review."))

        attrs['reviewer'] = reviewer
        return attrs

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['reviewer'] = userSerializer.UserIdAndNameSerializer(
            instance.reviewer, many=False).data
        return representation


class MovieSerializer(serializers.ModelSerializer):
    average_vote = serializers.SerializerMethodField(read_only=True)
    reviews = serializers.SerializerMethodField(read_only=True)
    casts = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Movie
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(
            MovieSerializer, self).to_representation(instance)
        representation['language'] = instance.language.name
        representation['rating'] = instance.rating.name
        representation['genre'] = GenreSerializer(
            instance.genre.all(), many=True).data
        representation['production'] = ProductionSerializer(
            instance.production.all(), many=True).data
        return representation

    def get_average_vote(self, obj):
        avg_vote = obj.review_set.all().aggregate(Avg('vote'))
        return round(avg_vote.get('vote__avg'), 1)

    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data

    def get_casts(self, obj):
        casts = obj.cast_set.all()
        serializer = CastMovieDetailSerializer(casts, many=True)
        return serializer.data


class ProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Production
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['person'] = nameSerializer.PersonSerializer(
            instance.person.all(), many=True).data
        return representation


class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cast
        fields = '__all__'


class CastMovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cast
        fields = ['id', 'character', 'person', 'profession']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['person'] = nameSerializer.PersonNameSerializer(
            instance.person, many=False).data
        representation['profession'] = instance.profession.type
        return representation
