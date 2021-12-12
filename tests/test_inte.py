import pytest
import src.app
from src.app import app

from flask import url_for

@pytest.fixture
def client():
    client = app.test_client()

    with app.app_context():
        pass

    app.app_context().push()
    return client

def test_index(client):
    var = client.get('/')
    assert var.status_code == 200
    # assert rv.status_code == 405
