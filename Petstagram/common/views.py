from django.shortcuts import render, redirect, resolve_url
import pyperclip

from Petstagram.common.models import Like
from Petstagram.photos.models import Photo


def index(request):
    all_photos = Photo.objects.all()
    context = {
        'all_photos': all_photos
    }
    return render(request, 'common/home-page.html', context)


def like_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    liked_object = Like.objects.filter(to_photo_id=photo_id).first()
    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo=photo)
        like.save()
    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def copy_link_to_clipboard(request, photo_id):
    pyperclip.copy(request.META['HTTP_HOST'] + resolve_url('details photo', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')
