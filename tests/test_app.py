import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    return app.test_client()


def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {'status': 'ok'}


def test_create_and_list_todos(client):
    created = client.post('/todos', json={'title': 'Finish DevOps assignment'})
    assert created.status_code == 201
    assert created.json['title'] == 'Finish DevOps assignment'
    listed = client.get('/todos')
    assert listed.status_code == 200
    assert len(listed.json) == 1


def test_reject_empty_title(client):
    response = client.post('/todos', json={'title': '  '})
    assert response.status_code == 400
