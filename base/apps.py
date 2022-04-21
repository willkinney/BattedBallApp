from django.apps import AppConfig


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # define the class name to be referred to in settings.py
    name = 'base'
