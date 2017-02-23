from django import forms
from django.forms import ModelForm

from post.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class PostForm(forms.Form):
    content = forms.CharField(required=False)
    photo = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


# class FileFieldForm(forms.Form):
#     file_field = forms.FileField()




    # class Meta:
    #     model=Post
    #     fields = ['photo',]
