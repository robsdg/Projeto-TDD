from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user_integration():
    response = client.post("/users", json={"name": "Robson", "email": "robson@email.com"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Robson"
    assert "_id" in data
