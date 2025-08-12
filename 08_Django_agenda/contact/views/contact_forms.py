from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from contact.forms import ContactForm
from contact.models import Contact


# Função para criar um novo contato (usuário precisa estar logado)
@login_required(login_url='contact:login')
def create(request):
    form_action = reverse('contact:create')

    if request.method == 'POST':
        # Cria o formulário com os dados enviados pelo usuário
        form = ContactForm(request.POST, request.FILES)

        context = {
            'form': form,
            'form_action': form_action,
        }

        # Se o formulário for válido, salva o contato e redireciona para a página de edição
        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            return redirect('contact:update', contact_id=contact.pk)

        # Se não for válido, renderiza o formulário novamente com erros
        return render(
            request,
            'contact/create.html',
            context
        )

    # Se não for POST, exibe o formulário vazio para criação
    context = {
        'form': ContactForm(),
        'form_action': form_action,
    }

    return render(
        request,
        'contact/create.html',
        context
    )


# Função para atualizar um contato existente (usuário precisa ser o dono)
@login_required(login_url='contact:login')
def update(request, contact_id):
    # Busca o contato pelo id, show=True e owner igual ao usuário logado
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True, owner=request.user
    )
    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':
        # Cria o formulário com os dados enviados e o contato existente
        form = ContactForm(request.POST, request.FILES, instance=contact)

        context = {
            'form': form,
            'form_action': form_action,
        }

        # Se o formulário for válido, salva as alterações e redireciona para a edição
        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)

        # Se não for válido, renderiza o formulário novamente com erros
        return render(
            request,
            'contact/create.html',
            context
        )

    # Se não for POST, exibe o formulário preenchido com os dados do contato
    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action,
    }

    return render(
        request,
        'contact/create.html',
        context
    )


# Função para deletar um contato (usuário precisa ser o dono)
@login_required(login_url='contact:login')
def delete(request, contact_id):
    # Busca o contato pelo id, show=True e owner igual ao usuário logado
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True, owner=request.user
    )
    # Verifica se o usuário confirmou a exclusão
    confirmation = request.POST.get('confirmation', 'no')

    # Se confirmado, deleta o contato e redireciona para a lista de contatos
    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')

    # Se não confirmado, renderiza a página de confirmação
    return render(
        request,
        'contact/contact.html',
        {
            'contact': contact,
            'confirmation': confirmation,
        }
    )
