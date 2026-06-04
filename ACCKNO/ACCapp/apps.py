from django.apps import AppConfig


class AccappConfig(AppConfig):
    name = "ACCapp"
    
    def ready(self):
        import ACCapp.signals