from django.apps import AppConfig


class ApplicationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.applications'

    def ready(self):
        import apps.applications.signals  # 👈 this line activates the signal
