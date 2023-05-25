from django.contrib import admin

from Petstagram.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'publication_date', 'description', 'pets')

    # We cannot list a Many-to-Many field, but we can list the result of a function that gets all objects from a
    # Many-to-Many field and concatenate their names in a string
    @staticmethod
    def pets(obj):
        tagged_pets = obj.tagged_pets.all()
        if tagged_pets:
            return ', '.join(pet.name for pet in tagged_pets)
        return 'No tagged Pets'
