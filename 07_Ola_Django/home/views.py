from django.shortcuts import render


def home(request):
    print('home')

    context = {
        'text': 'Olá Django primeiro projeto',
    }

    # Puxando o HTML do template
    return render(
        request,
        'home/index.html',
        context,
    )
