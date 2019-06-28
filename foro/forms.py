from django import forms

from .models import Post, Comentario


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('titulo', 'texto',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ('autor', 'texto',)
