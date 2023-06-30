from django.urls import path, include

from Petstagram.accounts.views import SignUpView, SignInView, SignOutView, \
    UserDetailsView, UserEditView, UserDeleteView

urlpatterns = [
    path('login/', SignInView.as_view(), name='login user'),
    path('logout/', SignOutView.as_view(), name='logout user'),
    path('register/', SignUpView.as_view(), name='register user'),
    path('profile/<int:pk>/', include([
        path('edit/', UserEditView.as_view(), name='edit user'),
        path('', UserDetailsView.as_view(), name='details user'),
        path('delete/', UserDeleteView.as_view(), name='delete user'),
    ])),
]
