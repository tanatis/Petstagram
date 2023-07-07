from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model, login

from Petstagram.accounts.forms import AppUserCreateForm, UserEditForm, AppUserLoginForm

# !!! Always get the 'user model' with 'get_user_model()'  !!!
UserModel = get_user_model()


class SignInView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    # In order to have custom placeholders or labels ... have to create a form in forms.py
    form_class = AppUserLoginForm


class SignUpView(views.CreateView):
    model = UserModel
    form_class = AppUserCreateForm
    template_name = 'accounts/register-page.html'
    #success_url = reverse_lazy('index')

    # Automatically login after registration:
    def form_valid(self, form):
        result = super().form_valid(form)
        user = self.object
        login(self.request, user)
        return result

    def get_success_url(self):
        return reverse_lazy('index')


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('login user')


class UserDetailsView(views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        # Проверяваме дали има качена снимка или да покажем дефолтната
        # в темплейта подаваме само {{ profile_picture }}
        # а проверките ги правим тук, вместо в темплейта
        # profile_picture = static('images/person.png')
        # if self.object.profile_picture is not None:
        #     profile_picture = self.object.profile_picture

        context = super().get_context_data(**kwargs)
        #context['profile_picture'] = profile_picture
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

