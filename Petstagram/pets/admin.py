from django.contrib import admin

from Petstagram.pets.models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug', 'date_of_birth', 'personal_photo',)
