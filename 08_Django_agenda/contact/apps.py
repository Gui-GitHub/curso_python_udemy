from django.apps import AppConfig

# Esse arquivo configura o aplicativo Django para a agenda de contatos
class ContactConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contact'
