from django.urls import path, include

from Petstagram.pets.views import add_pet, details_pet, edit_pet, delete_pet

urlpatterns = [
    path('add/', add_pet, name='add pet'),
    path('<str:username>/pet/<slug:slug>/', include([
        path('', details_pet, name='details pet'),
        path('edit/', edit_pet, name='edit pet'),
        path('delete/', delete_pet, name='delete pet'),
    ]))
]
