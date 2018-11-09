import os

from django.core.handlers.wsgi import WSGIHandler

from .wsgi import application
from .urls import urlpatterns as url
from myideas.core.urls import urlpatterns as url_core
from myideas.api.urls import urlpatterns as url_api
from myideas.core.apps import CoreConfig


def test_app():
    assert CoreConfig.name == 'core'


def test_urls_len():
    assert 6 == len(url)


def test_urls_core_len():
    assert 7 == len(url_core)


def test_urls_api_len():
    assert 3 == len(url_api)


def test_wsgi_default_settings():
    assert 'myideas.settings' == os.environ["DJANGO_SETTINGS_MODULE"]


def test_application_instace():
    assert isinstance(application, WSGIHandler)
