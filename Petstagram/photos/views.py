from django.shortcuts import render, redirect

from Petstagram.common.forms import CommentForm
from Petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from Petstagram.photos.models import Photo


def add_photo(request):
    if request.method == 'GET':
        form = PhotoCreateForm()
    else:
        form = PhotoCreateForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save()  # form.save връща обекта с който работи. Ползваме го долу да вземем pk
            return redirect('details photo', pk=photo.pk)

    context = {
        'form': form
    }
    return render(request, 'photos/photo-add-page.html', context)


def details_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    likes = photo.like_set.all()
    comments = photo.comment_set.all()
    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
        'comment_form': CommentForm()
    }

    return render(request, 'photos/photo-details-page.html', context)


def edit_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = PhotoEditForm(instance=photo)
    else:
        form = PhotoEditForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            photo = form.save()
            return redirect('details photo', pk=photo.pk)
    context = {
        'form': form,
        'photo': photo
    }
    return render(request, 'photos/photo-edit-page.html', context)


def delete_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    photo.delete()

    return redirect('index')


# def add_comment(request, pk):
#     photo = Photo.objects.filter(pk=pk).get()
#     form = CommentForm(request.POST)
#     if form.is_valid():
#         comment = form.save(commit=False)
#         comment.to_photo = photo
#         comment.save()
#
#     return redirect('details photo', pk=photo.pk)
