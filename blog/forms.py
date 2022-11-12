from django import forms
from .models import Post
class CommentForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'body', 'categories']

    