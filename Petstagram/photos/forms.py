from django import forms

from Petstagram.photos.models import Photo


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('publication_date', 'user')


class PhotoCreateForm(PhotoBaseForm):
    pass


class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('photo', 'user')


class PhotoDeleteForm(PhotoBaseForm):
    pass
