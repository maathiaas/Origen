from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_view, name='posts'),
    path('post/nuevo/', views.post_new, name='nuevo_post'),
    path('post/<int:pk>/', views.post_detail, name='detalle_post'),
    # path('post/<int:pk>/edit/', views.post_edit, name='detalle_post'),
    path('post/<int:pk>/comentario/',
         views.añadir_comentario, name='añadir_comentario'),
    # path('comentario/<int:pk>/aprobar/',
    #      views.comentario_aprobado, name='comentario_aprobado'),
    # path('comentario/<int:pk>/borrar/',
    #      views.borrar_comentario, name='borrar_comentario'),



]
