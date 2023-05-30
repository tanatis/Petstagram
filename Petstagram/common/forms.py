from django import forms

from Petstagram.common.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(
                attrs={'placeholder': 'Add comment', 'cols': 40, 'rows': 10}
            )
        }


class SearchForm(forms.Form):
    pet_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search by pet name ...'
            }
        )
    )