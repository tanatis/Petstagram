from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

UserModel = get_user_model()


class Pet(models.Model):
    MAX_NAME = 30
    name = models.CharField(max_length=MAX_NAME, null=False, blank=False)
    personal_photo = models.URLField(null=False, blank=False)
    date_of_birth = models.DateField(blank=True, null=True)
    slug = models.SlugField(unique=True, null=False, blank=True, editable=False)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  #първо правим запис за да може да си вземе ID инъче прави slug: none-name
        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.name}')
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.id} {self.name}'
