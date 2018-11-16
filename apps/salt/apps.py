from django.apps import AppConfig


class SaltConfig(AppConfig):
    name = 'salt'
    verbose_name = "SALT"
    def ready(self):
        import salt.signals
