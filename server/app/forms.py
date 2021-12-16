from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Comment, Post, Letter


class LetterForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    message = forms.CharField(max_length=300)


class UserForm(forms.Form):
    username = forms.CharField(max_length=40, min_length=10, required=True)
    password = forms.CharField(max_length=40, min_length=10, required=True)
    email = forms.EmailInput()

    def __init__(self, is_login):
        super().__init__()
        self.is_login = is_login

    def clean_email(self):
        email = self.cleaned_data['email']

        if not len(email) and self.is_login:
            return email

        user = User.objects.filter(email=email)

        if user.exists():
            raise ValidationError("User with such email is already in our database")

        return email


class CommentForm(forms.Form):
    post_id = forms.IntegerField(max_value=300, min_value=1)

    def clean_post_id(self):
        post_id = self.cleaned_data['post_id']
        post = Post.objects.filter(id=int(post_id))

        if post is None:
            raise ValidationError("Invalid post id")

        return post_id

    class Meta:
        model = [Comment]


