from typing import Any

from blog.data import posts
from django.http import Http404, HttpRequest
from django.shortcuts import render


def blog(request):
    print('blog')

    context = {
        # Utilizando a variável posts de data.py
        'posts': posts
    }

    return render(
        request,
        'blog/index.html',
        context
    )

# Função para que o id funcione como parâmetro na URL
def post(request: HttpRequest, post_id: int):
    found_post: dict[str, Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    # Se não encontrar o post, lança um erro 404
    if found_post is None:
        raise Http404('Post não existe.')

    context = {
        'post': found_post,
        'title': found_post['title'] + ' - ',
    }

    return render(
        request,
        'blog/post.html',
        context
    )


def exemplo(request):
    print('exemplo')

    context = {
        'text': 'Olá exemplo blog',
        'title': 'Essa é uma página de exemplo - ',
    }

    return render(
        request,
        'blog/exemplo.html',
        context
    )
