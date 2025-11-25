from fastapi.testclient import TestClient


def test_root(client: TestClient) -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Country API lab is running"}


def test_external_raw_default_ip(client: TestClient) -> None:
    response = client.get("/external/data")
    # external API may be unavailable, but route should exist and not 404.
    assert response.status_code in (200, 400, 422, 500)
