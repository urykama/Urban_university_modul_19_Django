from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'task1'
urlpatterns = [
    # представления поста
    path('', TemplateView.as_view(template_name='platform.html')),
    path('sign_up/', views.sign_up),
    path('platform/', TemplateView.as_view(template_name='platform.html')),
    path('games/', views.games, name='task1/games'),
    path('cart/', views.cart, name='task1/cart'),
]
