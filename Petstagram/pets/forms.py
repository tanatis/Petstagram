from django import forms

from Petstagram.pets.models import Pet


# Правим една базова форма за да могат другите да наследяват нея, а не да се наследяват взаимно
class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        # Не ни трябва полето slug защото го генерираме автоматично в модела
        # Ползваме fields вместо exclude за да можем да ги подредим както искаме
        fields = ['name', 'date_of_birth', 'personal_photo']
        labels = {
            'name': 'Pet Name',
            'date_of_birth': 'Date of birth',
            'personal_photo': 'Link to image'
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Pet name'
                }
            ),
            'personal_photo': forms.URLInput(
                attrs={
                    'placeholder': 'Link to image'
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'placeholder': 'dd-----yyyy',
                    'type': 'date'
                }
            )
        }


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(PetBaseForm):
    pass


class PetDeleteForm(PetBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            #field.widget.attrs['disabled'] = 'disabled'  # Това пречи  да се изтрие от базата, затова го закоментираме
            field.widget.attrs['readonly'] = 'readonly'

    # Променяме логиката на save (само на тази форма) не да запазва, а да изтрива
    def save(self, commit=True):
        if commit:
            self.instance.delete()
        else:
            pass