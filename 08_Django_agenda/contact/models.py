from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# id (primary key - automático)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)
# category (foreign key), show (boolean), picture (imagem)
# owner (foreign key)

# Aqui no models criamos as classes que representam as tabelas do banco de dados.
class Category(models.Model):
    # Classe meta para definir o nome da tabela e plural para o Admin do Django
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

# Configurando os fiels
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True) # blank=True permite que o campo seja opcional
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True) # Já inicia o campo como True
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/') # Caminho + ano + mês atual
    category = models.ForeignKey( # Configurando uma chave estrangeira
        Category,
        on_delete=models.SET_NULL, # O que acontece caso algum dado da Category seja apagado
        blank=True, null=True
    )
    owner = models.ForeignKey( # A pessoa que criou o perfil, poderá edita-lo
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
