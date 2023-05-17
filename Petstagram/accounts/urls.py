from django.urls import path, include

from Petstagram.accounts.views import login_user, register_user, edit_user, details_user, delete_user

urlpatterns = [
    path('login/', login_user, name='login user'),
    path('register/', register_user, name='register user'),
    path('profile/<int:pk>/', include([
        path('edit/', edit_user, name='edit user'),
        path('', details_user, name='details user'),
        path('delete/', delete_user, name='delete user'),
    ])),
]