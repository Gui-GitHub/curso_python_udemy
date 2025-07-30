from blog import views
from django.urls import path

# Dando nome ao app, para usarmos por exemplo blog:blog
# Isso é importante para evitar conflitos de nomes entre apps
app_name = 'blog'

# blog/
# Django URLs:
# https://docs.djangoproject.com/en/4.2/topics/http/urls/
# Colocando 'name=' para usar no HTML por exemplo
# {% url 'blog:home' %}

urlpatterns = [
    path('', views.blog, name='home'),
    path('<int:post_id>/', views.post, name='post'),
    path('exemplo/', views.exemplo, name='exemplo'),
]
