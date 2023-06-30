from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from Petstagram.pets.models import Pet
from Petstagram.photos.validators import validate_image_less_than_5mb

UserModel = get_user_model()


class Photo(models.Model):

    photo = models.ImageField(
        validators=(validate_image_less_than_5mb,),
        upload_to='pet_photos/',
        null=False,
        blank=False
    )
    description = models.TextField(
        max_length=300,
        validators=(MinLengthValidator(10),),
        null=True,
        blank=True
    )
    location = models.CharField(max_length=30, null=True, blank=True)
    publication_date = models.DateField(auto_now=True, null=False, blank=True)  # `auto_now` sets the current date on save

    # One-to-One

    # One-to_Many
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    # Many-to-Many
    tagged_pets = models.ManyToManyField(Pet, blank=True)

