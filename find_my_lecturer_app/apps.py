from django.apps import AppConfig


class FindMyLecturerAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'find_my_lecturer_app'

    def ready(self):
        import find_my_lecturer_app.signals  # 
