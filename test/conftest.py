import pytest
import domain.factory

@pytest.fixture
def client():
    app = domain.factory.create_app()
    return app.test_client()