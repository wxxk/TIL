from dataclasses import field
from turtle import width
from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["title", "content"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control mt-2",
                }
            ),
            "content": forms.Textarea(attrs={"class": "form-control mt-2", "rows": 10}),
        }
        labels = {
            "title": "제목",
            "content": "내용",
        }
