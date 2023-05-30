from django.shortcuts import render, redirect, resolve_url
import pyperclip

from Petstagram.common.forms import CommentForm, SearchForm
from Petstagram.common.models import Like
from Petstagram.photos.models import Photo


def index(request):
    all_photos = Photo.objects.all()
    comment_form = CommentForm()
    search_form = SearchForm(request.GET)

    search_pattern = None
    if search_form.is_valid():
        search_pattern = search_form.cleaned_data['pet_name']
        
    if search_pattern:
        all_photos = all_photos.filter(tagged_pets__name__icontains=search_pattern)

    context = {
        'all_photos': all_photos,
        'comment_form': comment_form,
        'search_form': search_form
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


def add_comment(request, photo_id):
    # Първо инстанцираме фото по id за да можем да закачим коментара на точно това фото
    photo = Photo.objects.filter(pk=photo_id).get()
    # Тук дефакто нямаме GET заявка затова няма if 'GET' .... а директно инициализираме пост форма
    form = CommentForm(request.POST)
    if form.is_valid():
        # Така сейфаме формата без да я записваме в базата
        # защото ако пробваме джанго ще каже че не може да запази коментар
        # без фото (всеки коментар е закачен за някое фото)
        comment = form.save(commit=False)
        comment.to_photo = photo  # Set-ваме фото на този коментар
        comment.save()            # Запазваме в базата

    return redirect(request.META['HTTP_REFERER'])
