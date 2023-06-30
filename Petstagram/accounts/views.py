from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model

from Petstagram.accounts.forms import AppUserCreateForm, UserEditForm

# !!! Always get the 'user model' with 'get_user_model()'  !!!
UserModel = get_user_model()


class SignInView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'


class SignUpView(views.CreateView):
    model = UserModel
    form_class = AppUserCreateForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('login user')


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('login user')


class UserDetailsView(views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object
        context['pets_count'] = self.object.pet_set.count()

        photos = self.object.photo_set.prefetch_related('like_set')

        context['photos_count'] = photos.count()
        context['likes_count'] = sum(x.like_set.count() for x in photos)
        context['photos'] = self.object.photo_set.all()

        return context


class UserEditView(views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'username', 'email', 'gender')

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={'pk': self.object.pk})


class UserDeleteView(views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')

