from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    
    # Importamos el archivo de signals para que se ejecuten y carguen al inicio de la app
    def ready(self):
        import accounts.signals.user_signals
