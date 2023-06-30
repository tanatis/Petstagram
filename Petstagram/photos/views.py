from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Petstagram.common.forms import CommentForm
from Petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from Petstagram.photos.models import Photo


@login_required
def add_photo(request):
    if request.method == 'GET':
        form = PhotoCreateForm()
    else:
        form = PhotoCreateForm(request.POST, request.FILES)
        if form.is_valid():
            #photo = form.save()  # form.save връща обекта с който работи. Ползваме го долу да вземем pk
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            form.save_m2m()
            return redirect('details photo', pk=photo.pk)

    context = {
        'form': form
    }
    return render(request, 'photos/photo-add-page.html', context)


def details_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    user_like_photos = Photo.objects.filter(pk=pk, user_id=request.user.pk)
    comments = photo.comment_set.all()
    context = {
        'photo': photo,
        'has_user_liked_photo': user_like_photos,
        'likes_count': photo.like_set.count(),
        'comments': comments,
        'comment_form': CommentForm(),
        'is_owner': photo.user == request.user
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
