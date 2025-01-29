from fastapi import FastAPI
from fastapi.testclient import TestClient
from .config import Settings, get_settings
from .routers.data import router


sub_app = FastAPI()

sub_app.include_router(router)

client = TestClient(sub_app)


def get_settings_override():
    return Settings(
        email_value="test@gmail.com",
        csrf_trusted_origins="*",
        allowed_hosts="*",
        github_url="https://github.com",
    )


sub_app.dependency_overrides[get_settings] = get_settings_override


def test_read_data():
    response = client.get("/api/v1/data")
    print(response.status_code, response.text)
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@gmail.com"
    assert data["github_url"] == "https://github.com"
    assert data["current_datetime"] is not None
