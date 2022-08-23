import pytest
from app import create_app


@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture(scope="session")
def image_path():
    path = "tests/images/1.jpeg"
    return path


@pytest.fixture(scope="session")
def invalid_image_path():
    path = "tests/images/dash.bmp"
    return path
