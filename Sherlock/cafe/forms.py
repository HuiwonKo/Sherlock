from django import forms

from .models import

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewForm
        fields = ('author','content', 'score_hard', 'score_star',)