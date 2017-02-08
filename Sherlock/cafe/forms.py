from django import forms
from .models import Cafe, Room, Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('author','content', 'score_hard', 'score_star',)