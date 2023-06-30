from django.urls import path

from Petstagram.common.views import index, like_photo, copy_link_to_clipboard, add_comment

urlpatterns = [
    path('', index, name='index'),
    path('like/<int:photo_id>/', like_photo, name='like'),
    path('share/<int:photo_id>/', copy_link_to_clipboard, name='share'),
    path('comment/<int:photo_id>/', add_comment, name='add comment'),
]
