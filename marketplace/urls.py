from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('allproduct/',views.Productos, name='producto'),
    path('ofertas/',views.Ofertas, name='oferta'),
]

