from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from contact.forms import RegisterForm, RegisterUpdateForm

# Função para registrar um novo usuário
def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        # Preenche o formulário com os dados enviados
        form = RegisterForm(request.POST)

        # Se o formulário for válido, salva o usuário e exibe mensagem de sucesso
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado')
            return redirect('contact:login')

    # Renderiza o formulário de registro
    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )

# Função para atualizar os dados do usuário logado
@login_required(login_url='contact:login')
def user_update(request):
    # Preenche o formulário com os dados do usuário atual
    form = RegisterUpdateForm(instance=request.user)

    # Se não for POST, apenas exibe o formulário preenchido
    if request.method != 'POST':
        return render(
            request,
            'contact/user_update.html',
            {
                'form': form
            }
        )

    # Se for POST, atualiza o formulário com os dados enviados
    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    # Se o formulário não for válido, renderiza novamente com erros
    if not form.is_valid():
        return render(
            request,
            'contact/user_update.html',
            {
                'form': form
            }
        )

    # Salva as alterações e redireciona para a mesma página
    form.save()
    return redirect('contact:user_update')

# Função para login do usuário
def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        # Preenche o formulário com os dados enviados
        form = AuthenticationForm(request, data=request.POST)

        # Se o formulário for válido, faz login e redireciona para a página inicial
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logado com sucesso!')
            return redirect('contact:index')
        # Se não for válido, exibe mensagem de erro
        messages.error(request, 'Login inválido')

    # Renderiza o formulário de login
    return render(
        request,
        'contact/login.html',
        {
            'form': form
        }
    )

# Função para logout do usuário logado
@login_required(login_url='contact:login')
def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')
