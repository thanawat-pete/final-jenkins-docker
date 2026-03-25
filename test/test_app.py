import pytest
from app import app


@pytest.fixture
def client():
    """สร้าง test client สำหรับ Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_hello_endpoint(client):
    """ทดสอบ API endpoint /api/hello"""
    response = client.get('/api/hello')
    
    # ตรวจสอบ status code
    assert response.status_code == 200
    
    # ตรวจสอบ response data
    json_data = response.get_json()
    assert json_data is not None
    assert json_data['message'] == 'Hello from Thanawat'


def test_me_endpoint(client):
    """ทดสอบ API endpoint /api/me"""
    response = client.get('/api/me')
    
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data is not None
    assert json_data['message'] == 'My name is Thanawat Srisaeng'


def test_health_endpoint(client):
    """ทดสอบ API endpoint /api/health"""
    response = client.get('/api/health')
    
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    json_data = response.get_json()
    assert json_data is not None
    assert json_data['message'] == 'up'


def test_goodbye_endpoint(client):
    """ทดสอบ API endpoint /api/goodbye"""
    response = client.get('/api/goodbye')
    
    # ตรวจสอบ status code
    assert response.status_code == 200
    
    # ตรวจสอบ response data
    json_data = response.get_json()
    assert json_data is not None
    assert json_data['message'] == 'Goodbye from Flask API!'


def test_hello_endpoint_method_not_allowed(client):
    """ทดสอบ HTTP method ที่ไม่อนุญาต"""
    response = client.post('/api/hello')
    assert response.status_code == 405  # Method Not Allowed


def test_non_existent_endpoint(client):
    """ทดสอบ endpoint ที่ไม่มีอยู่"""
    response = client.get('/api/notfound')
    assert response.status_code == 404  # Not Found