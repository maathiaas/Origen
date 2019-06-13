from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.


def post_view(request):
    posts = Post.objects.filter(
        fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')

    return render(request, 'foro/post_list.html', {'posts': posts})
