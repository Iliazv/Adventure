from logging import PlaceHolder
from django import forms
from .models import *
from ckeditor.fields import RichTextField

         
class PostCommentary(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Ваше имя'
        self.fields['text'].label = 'Текст комментария'
    
    class Meta:
        model = Comment
        fields = ('name', 'text')
        
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'myfieldclass', 'placeholder': 'Написать имя'}),
            'text': forms.Textarea(attrs={'class': 'myfieldclass', 'placeholder': 'Написать отзыв'}),
        }

class PostResponse(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].label = 'Ваше имя'
        self.fields['user_text'].label = 'Текст комментария'
    
    class Meta:
        model = Response
        fields = ('user_name', 'user_text')
        
        
        widgets = {
            'user_name': forms.TextInput(attrs={'class': 'myfieldclass', 'placeholder': 'Написать имя'}),
            'user_text': forms.Textarea(attrs={'class': 'myfieldclass', 'placeholder': 'Написать отзыв'}),

        }