from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UsernameField

UserModel = get_user_model()


class UserEditForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = '__all__'
        field_classes = {'username': UsernameField}


class AppUserCreateForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email')
        field_classes = {'username': UsernameField}
