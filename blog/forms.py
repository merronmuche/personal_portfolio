from django import forms
from .models import Post
class CommentForm(forms.Form):
    body = forms.CharField(max_length=255)
    

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'body', 'categories']

    