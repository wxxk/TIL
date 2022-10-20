from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'movie_name', 'content', 'grade',)


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        exclude = ('review', 'user',)
