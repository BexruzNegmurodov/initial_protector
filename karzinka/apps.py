from django.apps import AppConfig


class KarzinkaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'karzinka'

    def ready(self):
        import karzinka.signals
