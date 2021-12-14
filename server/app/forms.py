from django import forms
from django.core.exceptions import ValidationError
from .models import Comment, Post, Letter


class LetterForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    message = forms.CharField(max_length=300)


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


