from app.app import app


def test_home_endpoint():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert response.json["application"] == "DevOps Platform Lab"


def test_health_endpoint():
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_version_endpoint():
    response = app.test_client().get("/version")
    assert response.status_code == 200
    assert response.json["version"] == "local"
