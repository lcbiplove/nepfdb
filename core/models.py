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

    id = models.BigIntegerField(primary_key=True)

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


class User(AbstractBaseUser, PermissionsMixin, AutoId):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    pp = models.ImageField(upload_to='photos/pp')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['name', ]
