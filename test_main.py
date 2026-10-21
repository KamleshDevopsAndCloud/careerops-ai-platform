
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_unknown_endpoint():
    response = client.get("/not-found")

    assert response.status_code == 404


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["application"] == "CareerOps"
