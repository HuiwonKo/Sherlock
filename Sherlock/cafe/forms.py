from django import forms
from .models import Cafe, Room, Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content']
        widgets = {
            'content' : forms.Textarea(attrs = {'class':'form-control', 'row':3})
        }