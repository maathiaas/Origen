from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from .models import Post, Comentario
from .forms import PostForm, CommentForm

# Create your views here.


def post_view(request):
    posts = Post.objects.filter(
        fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')

    return render(request, 'foro/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'foro/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.fecha_publicacion = timezone.now()
            post.save()
            return redirect('detalle_post', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'foro/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.fecha_publicacion = timezone.now()
            post.save()
            return redirect('detalle_post', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'foro/post_edit.html', {'form': form})


def añadir_comentario(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.save()
            return redirect('detalle_post', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'foro/añadir_comentario.html', {'form': form})


# def comentario_aprobado(request, pk):
#     comentario = get_object_or_404(Comentario, pk=pk)
#     comentario.aprobar()
#     return redirect('detalle_post', pk=comentario.post.pk)


# def borrar_comentario(request, pk):
#     comentario = get_object_or_404(Comentario, pk=pk)
#     comentario.delete()
#     return redirect('detalle_post', pk=comentario.post.pk)
