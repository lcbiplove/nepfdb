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
    reviewers = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Review
        fields = '__all__'
        extra_kwargs = {
            "reviewer": {"read_only": True, },
        }

    def get_reviewers(self, obj):
        obj = userSerializer.UserIdAndNameSerializer(
            obj.reviewer, many=False).data
        return obj

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


class MovieBasicSerializer(serializers.ModelSerializer):
    average_vote = serializers.SerializerMethodField(read_only=True)
    photo = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Movie
        fields = '__all__'
        abstract = True

    def get_average_vote(self, obj):
        avg_vote = obj.review_set.all().aggregate(Avg('vote'))
        return round(avg_vote.get('vote__avg'), 1)

    def get_photo(self, obj):
        try:
            obj = obj.photo_set.first().link
        except:
            obj = None
        return obj


class MovieSerializer(MovieBasicSerializer):
    casts = serializers.SerializerMethodField(read_only=True)
    reviews = serializers.SerializerMethodField(read_only=True)
    awards = serializers.SerializerMethodField(read_only=True)
    photos = serializers.SerializerMethodField(read_only=True)
    language_name = serializers.SerializerMethodField(read_only=True)
    rating_type = serializers.SerializerMethodField(read_only=True)
    genres = serializers.SerializerMethodField(read_only=True)
    productions = serializers.SerializerMethodField(read_only=True)

    def get_casts(self, obj):
        casts = obj.cast_set.all()
        serializer = CastMovieDetailSerializer(casts, many=True)
        return serializer.data

    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data

    def get_awards(self, obj):
        data = None
        cast = models.AwardCategory.objects.filter(
            cast__in=obj.cast_set.all()).all() or None
        movie = obj.awardcategory_set.all() or None

        if cast or movie:
            total = 0
            wins = 0
            if movie:
                total += movie.count()
                wins += movie.filter(isWinner=True).count()
            if cast:
                total += cast.count()
                wins += cast.filter(isWinner=True).count()

            data = {
                "wins": wins,
                "nominations": total,
            }
        return data

    def get_photos(self, obj):
        queryset = obj.photo_set.all()
        return [x.link for x in queryset]

    def get_language_name(self, obj):
        return obj.language.name

    def get_rating_type(self, obj):
        return obj.rating.name

    def get_genres(self, obj):
        return GenreSerializer(
            obj.genre.all(), many=True).data

    def get_productions(self, obj):
        return ProductionSerializer(
            obj.production.all(), many=True).data


class ProductionSerializer(serializers.ModelSerializer):
    persons = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Production
        fields = '__all__'

    def get_persons(self, obj):
        obj = nameSerializer.PersonNameSerializer(
            obj.person.all(), many=True).data
        return obj


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
