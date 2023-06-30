from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from Petstagram.accounts.forms import UserEditForm, AppUserCreateForm

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    form = UserEditForm
    add_form = AppUserCreateForm

    # fieldsets = (
    #     (None, {'fields': ('username', 'password')}),
    #     ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'gender')}),
    #     ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')}),
    # )
