from django.apps import AppConfig


class SiteCatalogoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'site_catalogo'
    def ready(self):
        import site_catalogo.signals