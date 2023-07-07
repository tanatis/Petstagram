from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Petstagram.common.decorator import is_owner
from Petstagram.common.forms import CommentForm
from Petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from Petstagram.pets.models import Pet


def get_pet_by_name_and_username(slug, username):
    return Pet.objects.filter(slug=slug, user__username=username).get()


def details_pet(request, username, slug):
    # TODO: check this in workshop
    pet = get_pet_by_name_and_username(slug, username)
    all_photos = pet.photo_set.all()
    context = {
        'pet': pet,
        'all_photos': all_photos,
        'photos_count': all_photos.count(),
        #'comment_form': CommentForm(),
        'is_owner': pet.user == request.user,
    }
    return render(request, 'pets/pet-details-page.html', context)


@login_required
def add_pet(request):
    if request.method == 'GET':
        form = PetCreateForm()
    else:
        form = PetCreateForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)  # Създай pet но не го вкарвай в базата още
            pet.user = request.user  # This is the looged user
            pet.save()  # Към базата
            return redirect('details user', pk=request.user.pk)

    context = {
        'form': form,
    }
    return render(request, 'pets/pet-add-page.html', context)


@login_required()
def edit_pet(request, slug, username):
    pet = get_pet_by_name_and_username(slug, username)

    if not is_owner(request, pet):
        return redirect('details pet', username=request.user, slug=slug)

    if request.method == 'GET':
        form = PetEditForm(instance=pet)
    else:
        form = PetEditForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('details pet', username=request.user, slug=slug)

    context = {
        'form': form,
        'slug': slug,
        'username': username,
    }
    return render(request, 'pets/pet-edit-page.html', context)


@login_required()
def delete_pet(request, username, slug):
    pet = get_pet_by_name_and_username(slug, username)
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
