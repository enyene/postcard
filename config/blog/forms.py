from django.forms import ModelForm
from .models import Comment
from django import forms

class CommentForm(ModelForm):
    body = forms.CharField(max_length=500)
    class Meta:
        model = Comment
        fields = [
            'body'
        ]