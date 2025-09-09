from app import app

def test_root():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello,I am from Tekton Python CI/CD" in response.data
