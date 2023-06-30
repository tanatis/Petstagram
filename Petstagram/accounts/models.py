from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models

from Petstagram.accounts.validators import only_letters_validator


class Gender(Enum):
    male = 'Male'
    female = 'Female'
    DoNotShow = 'Do not Show'

    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

    @classmethod
    def max_length(cls):
        return max(len(name) for name, _ in cls.choices())


class AppUser(AbstractUser):
    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=30,
        validators=(MinLengthValidator(2), only_letters_validator,)
    )

    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=30,
        validators=(MinLengthValidator(2), only_letters_validator,)
    )

    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
    )

    gender = models.CharField(
        blank=False,
        null=False,
        choices=Gender.choices(),
        max_length=Gender.max_length(),
    )

    # Users logs in with email instead of username
    # USERNAME_FIELD = 'email'
