# import pytest
# from app import create_app
# from flask import Flask
# from urllib.parse import quote

# @pytest.fixture
# def app():
#     return create_app()

# @pytest.fixture
# def client(app):
#     return app.test_client()

# def test_home(client):
#     response = client.get('/')
#     assert response.status_code == 200
#     expected_text = 'Well done! You Successfully deployed your flask app, Now you can start building your app.'
#     assert expected_text.encode() in response.data

import pytest
from flask import Flask
from app import create_app  # Replace `your_module` with the actual module name where `create_app` is defined

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    expected_text = 'Well done! You Successfully added and deployed your flask app, Now you can start building your app.'
    assert expected_text.encode() in response.data
