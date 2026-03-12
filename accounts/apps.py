from django.apps import AppConfig

class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"

    def ready(self):
        # Eu importo os signals aqui pra eles funcionarem quando o app sobe
        import accounts.signals