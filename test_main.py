from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_profile():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == { "slackUsername": "ali-sani", "backend": True, "age": 27, "bio": 'I am software developer who is very passionate about enterpreneuship. I joined HNG9 for the challenge and community.' }
