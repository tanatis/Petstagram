from django.shortcuts import render

from Petstagram.pets.models import Pet


def add_pet(request):
    return render(request, 'pets/pet-add-page.html')


def delete_pet(request, username, slug):
    return render(request, 'pets/pet-delete-page.html')


def edit_pet(request, username, slug):
    return render(request, 'pets/pet-edit-page.html')


def details_pet(request, username, slug):
    pet = Pet.objects.get(slug=slug)
    all_photos = pet.photo_set.all()
    context = {
        'pet': pet,
        'all_photos': all_photos,
    }
    return render(request, 'pets/pet-details-page.html', context)
