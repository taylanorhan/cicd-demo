import pytest
import json
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['message'] == 'Merhaba Dünya!'

def test_status(client):
    response = client.get('/api/status')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert 'status' in data
    assert 'version' in data