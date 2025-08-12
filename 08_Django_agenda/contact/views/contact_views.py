from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from contact.models import Contact

# Essa função renderiza a página inicial com uma lista de contatos paginada
def index(request):
    # Busca todos os contatos com show=True e ordena por id decrescente
    contacts = Contact.objects \
        .filter(show=True)\
        .order_by('-id')

    # Paginação: 10 contatos por página
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos - '
    }

    # Renderiza o template com os contatos paginados
    return render(
        request,
        'contact/index.html',
        context
    )

# Função para buscar contatos com base no termo de pesquisa
def search(request):
    # Obtém o valor da pesquisa (query string 'q')
    search_value = request.GET.get('q', '').strip()

    # Se o valor de pesquisa estiver vazio, redireciona para a página inicial
    if search_value == '':
        return redirect('contact:index')

    # Filtra contatos pelo termo de pesquisa nos campos nome, sobrenome, telefone ou email
    contacts = Contact.objects \
        .filter(show=True)\
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value)
        )\
        .order_by('-id')

    # Paginação dos resultados da busca
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Search - ',
        'search_value': search_value,
    }

    # Renderiza o template com os resultados da busca
    return render(
        request,
        'contact/index.html',
        context
    )

# Exibe os detalhes de um contato específico
def contact(request, contact_id):
    # Busca o contato pelo id e garante que show=True, senão retorna 404
    single_contact = get_object_or_404(
        Contact, pk=contact_id, show=True
    )
    # Define o título da página com o nome do contato
    site_title = f'{single_contact.first_name} {single_contact.last_name} - '

    context = {
        'contact': single_contact,
        'site_title': site_title
    }

    # Renderiza o template de detalhes do contato
    return render(
        request,
        'contact/contact.html',
        context
    )
