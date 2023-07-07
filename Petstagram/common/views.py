from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, resolve_url
import pyperclip

from Petstagram.common.forms import CommentForm, SearchForm
from Petstagram.common.models import Like
from Petstagram.photos.models import Photo


def index(request):
    all_photos = Photo.objects.all().order_by('-pk')
    comment_form = CommentForm()
    search_form = SearchForm(request.GET)

    search_pattern = None
    if search_form.is_valid():
        search_pattern = search_form.cleaned_data['pet_name']
        
    if search_pattern:
        all_photos = all_photos.filter(tagged_pets__name__icontains=search_pattern)

    # На всяка снимка която е лайкната от юзъра и слагаме liked_by_user за да може в темплейта да не е
    # червена ако не е лайкната
    for photo in all_photos:
        photo.liked_by_user = photo.like_set.filter(user=request.user).exists()

    context = {
        'all_photos': all_photos,
        'comment_form': comment_form,
        'search_form': search_form
    }
    return render(request, 'common/home-page.html', context)


@login_required
def like_photo(request, photo_id):
    user_liked_photos = Like.objects.filter(to_photo_id=photo_id, user_id=request.user.pk)
    if user_liked_photos:
        user_liked_photos.delete()
    else:
        Like.objects.create(to_photo_id=photo_id, user_id=request.user.pk)

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def copy_link_to_clipboard(request, photo_id):
    pyperclip.copy(request.META['HTTP_HOST'] + resolve_url('details photo', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


@login_required()
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
        comment.user = request.user  # Set-ваме юзър за коментара
        comment.save()            # Запазваме в базата

    return redirect(request.META['HTTP_REFERER'],)
