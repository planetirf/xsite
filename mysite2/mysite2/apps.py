from importlib import import_module

from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):

    name = "mysite2"

    def ready(self):
        import_module("mysite2.receivers")
