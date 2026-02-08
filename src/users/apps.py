from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # Added function to activate signal when User is created 
    def ready(self):
        import users.signals