from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin
from django.urls import reverse
from django.utils.translation import gettext as _
from random import randint


RANDOM_ID_DIGITS = 16


class AutoId(models.Model):
    """Auto add a custom integer ids"""

    class Meta:
        abstract = True

    id = models.BigIntegerField(primary_key=True, editable=False)

    def save(self, *args, **kwargs):
        """Check if the user id is provided or not, create random unique
        if not provided"""

        if not self.id:
            is_unique = False
            while not is_unique:
                id = randint(10 ** (RANDOM_ID_DIGITS - 1),
                             10 ** RANDOM_ID_DIGITS)
                is_unique = not self.__class__.objects.filter(id=id).exists()
            self.id = id
        super(AutoId, self).save(*args, **kwargs)


class UserManager(BaseUserManager):

    def create_user(self, email, name, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(
            email), name=name, **extra_fields)

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creates and saves new superuser"""
        user = self.create_user(email, name, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin, models.Model, ):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    pp = models.ImageField(upload_to='photos/pp')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['name', ]

    def __str__(self):
        return str(self.email)


class Review(models.Model, ):
    """Review model to store review of the movie"""
    text = models.TextField(blank=True)
    vote = models.DecimalField(decimal_places=1, max_digits=3)
    reviewed_at = models.DateTimeField(auto_now_add=True)
    reviewer = models.ForeignKey('User', on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.movie.name} : {self.vote}"


class Language(models.Model):
    """Language of the movie"""
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, unique=True)
    country = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name)


class Genre(models.Model):
    """Genre/Category of the movie"""
    name = models.CharField(max_length=30, unique=True)
    desc = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Rating(models.Model):
    """Rating type of movie, eg: PG, PG-13"""
    name = models.CharField(max_length=10, unique=True)
    desc = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Movie(models.Model, ):
    """Model to contain movie details"""
    name = models.CharField(max_length=50)
    budget = models.DecimalField(
        decimal_places=2, max_digits=20, null=True, blank=True)
    summary = models.TextField()
    release_date = models.DateField()
    runtime = models.IntegerField(null=True, blank=True)
    boxoffice = models.DecimalField(
        decimal_places=2, max_digits=20, null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)
    genre = models.ManyToManyField('Genre')
    production = models.ManyToManyField(
        'Production')
    rating = models.ForeignKey('Rating', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    @property
    def year(self):
        return self.release_date.year


class Award(models.Model, ):
    """Award object"""
    name = models.CharField(max_length=50)
    first_year = models.IntegerField()

    def __str__(self):
        return str(self.name)


class AwardCategory(models.Model, ):
    """Award category for each award"""
    category = models.CharField(max_length=50)
    movie = models.ForeignKey(
        'Movie', on_delete=models.PROTECT, blank=True, null=True)
    cast = models.ForeignKey(
        'Cast', on_delete=models.PROTECT, blank=True, null=True)
    award = models.ForeignKey('Award', on_delete=models.PROTECT)
    isWinner = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Award Categories"

    def __str__(self):
        return str(self.category)


class Cast(models.Model):
    """Cast members of movie"""
    character = models.CharField(max_length=50, default="Cast")
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    profession = models.ForeignKey('Profession', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.character)


class Production(models.Model, ):
    """Production house object"""
    name = models.CharField(max_length=50)
    established_year = models.IntegerField()
    person = models.ManyToManyField('Person')

    def __str__(self):
        return str(self.name)


class Person(models.Model, ):
    """Artist associated with movie industry"""
    name = models.CharField(max_length=50)
    dob = models.DateField()
    nation = models.CharField(max_length=28)
    bio = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Profession(models.Model):
    """Profession of the artist, eg: director"""
    type = models.CharField(max_length=28)

    def __str__(self):
        return str(self.type)


class Photo(models.Model, ):
    """Photo/posters of artist or movie"""
    link = models.CharField(max_length=255)
    movie = models.ForeignKey(
        'Movie', on_delete=models.CASCADE, null=True, blank=True)
    person = models.ForeignKey(
        'Person', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.link)
