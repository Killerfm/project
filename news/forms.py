from .models import FirstTable, Commentaries
from django.forms import ModelForm, TextInput, DateInput, Textarea


class FirstTableForm(ModelForm):
    class Meta:
        model = FirstTable
        fields = ['name', 'main_text', 'date']
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'название',
            }),
            "main_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'основной текст',
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'дата'
            })
        }


class CommentariesForm(ModelForm):
    class Meta:
        model = Commentaries
        fields = ['author', 'commentary', 'date', 'nameb']
        widgets = {
            "author": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'автор',
            }),
            "commentary": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'основной текст',
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'дата'
            })

        }
