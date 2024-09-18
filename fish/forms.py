from .models import FirstTable
from django.forms import ModelForm, TextInput, DateInput, Textarea, FileInput


class FirstTableForm(ModelForm):
    class Meta:
        model = FirstTable
        fields = ['name', 'main_text', 'date', 'img']
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'name',
            }),
            "main_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'main text',
            }),
            "img": FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'image'
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'date'
            })
        }
