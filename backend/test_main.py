from fastapi.testclient import TestClient

from database import app

client = TestClient(app)
my_resolver = dns.resolver.Resolver()
answers = my_resolver.resolve(host, "A")
answer_txt = my_resolver.resolve(host, "TXT")
def f():
    return 4

def test_function():
    assert f() == 4

def test_read_main():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
