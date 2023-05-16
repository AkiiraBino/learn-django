from typing import Any, Dict
from django import forms
from .models import *

class AddPostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat_id'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Actresses
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat_id']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'rows': 10, 'cols': 60})
        }

    def clean_title(self):
        title = self.cleaned_data(['title'])
        if len(title) > 200:
            raise forms.ValidationError('Длина превышает 200 символов')
        
        return title