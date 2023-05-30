from django.shortcuts import render, redirect

from Petstagram.common.forms import CommentForm
from Petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from Petstagram.pets.models import Pet


def details_pet(request, username, slug):
    # TODO: check this in workshop
    pet = Pet.objects.get(slug=slug)
    all_photos = pet.photo_set.all()
    context = {
        'pet': pet,
        'all_photos': all_photos,
        'comment_form': CommentForm()
    }
    return render(request, 'pets/pet-details-page.html', context)


def add_pet(request):
    if request.method == 'GET':
        form = PetCreateForm()
    else:
        form = PetCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details user', pk=1)  # TODO: fix pk when auth

    context = {
        'form': PetCreateForm(),
    }
    return render(request, 'pets/pet-add-page.html', context)


def edit_pet(request, username, slug):
    # Тук трябва да заредим данните на селектирания пет във формата и затова първо го инстанцираме
    pet = Pet.objects.filter(slug=slug).get()  # TODO: use username when auth
    if request.method == 'GET':
        form = PetEditForm(instance=pet)
    else:
        form = PetEditForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('details pet', username='tanatis', slug=slug)

    context = {
        'form': form,
        'slug': slug,
        'username': username,
    }
    return render(request, 'pets/pet-edit-page.html', context)


def delete_pet(request, username, slug):
    pet = Pet.objects.filter(slug=slug).get()
    if request.method == 'GET':
        form = PetDeleteForm(instance=pet)
    else:
        form = PetDeleteForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()  # За да изтрием трябва този метод save да го overwrite в формата
            return redirect('details user', pk=1)  # TODO: fix pk when auth

    context = {
        'form': form,
        'username': username,
        'slug': slug,
    }

    return render(request, 'pets/pet-delete-page.html', context)
