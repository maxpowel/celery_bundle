import pytest
from celery import Celery

from celery_bundle.bundle import CeleryConfig, create_client


@pytest.fixture
def celery_config() -> CeleryConfig:
    return CeleryConfig(name='test-celery-app')


def test_create_client(celery_config: CeleryConfig):
    app = create_client(celery_config)
    assert isinstance(app, Celery)
    assert app.main == celery_config.name
