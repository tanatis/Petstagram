from django.contrib.auth import get_user_model
from django.db import models

from Petstagram.photos.models import Photo

UserModel = get_user_model()


class Comment(models.Model):
    text = models.TextField(max_length=300, blank=False, null=False)
    date_time_of_publication = models.DateTimeField(auto_now_add=True, null=False, blank=True)
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE, null=False, blank=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_time_of_publication']


class Like(models.Model):
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
