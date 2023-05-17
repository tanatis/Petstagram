from django.urls import path

from Petstagram.common.views import index

urlpatterns = [
    path('', index, name='index'),
]
