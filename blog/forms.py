from django import forms
from django.contrib.auth import get_user_model
from . import models


class PhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ['image', 'caption']

class PhotoForm(forms.ModelForm):
    edit_photo = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = models.Photo
        fields = ['image', 'caption']

class DeletePhotoForm(forms.Form):
    delete_photo = forms.BooleanField(widget=forms.HiddenInput, initial=True)

class BlogForm(forms.ModelForm):
    class Meta:
        model = models.Blog
        fields = ['title', 'lead', 'content', 'picture']

class BlogForm(forms.ModelForm):
    edit_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = models.Blog
        fields = ['title', 'lead', 'content', 'picture']


class DeleteBlogForm(forms.Form):
    delete_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)
