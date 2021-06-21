from fastapi.testclient import TestClient

import main 

client = TestClient(main.app)


def test_backend_status():
    response = client.get("/BackendStatus")
    assert response.status_code == 200
    assert response.json() == {"status": "running"}

def test_get_employee():
    response = client.get("/employee")
    assert response.json() == [{
        "_id":"60bd8e1919e14f69f3be08b1","name":"Jane Doe","email":"jdoe@example.com",
        "department":"IT","employee_details":"updatedetails","employee_risk_level":3.0},
        {"_id":"60bd8e2719e14f69f3be08b2","name":"ecy3","email":"ecy3@example.com","department":"IT",
        "employee_details":"details","employee_risk_level":3.0
        }]

def test_get_employee_id():
    response = client.get("/employee/60bd8e1919e14f69f3be08b1")
    assert response.json() == {
        "_id":"60bd8e1919e14f69f3be08b1","name":"Jane Doe","email":"jdoe@example.com",
        "department":"IT","employee_details":"updatedetails","employee_risk_level":3.0}
    
def test_create_employee():
    response = client.post(
        "/employee/",
        json={
            "name": "Jane Doe",
            "email": "jdoe@example.com",
            "department": "IT",
            "employee_details": "details",
            "employee_risk_level": "3.0"
        }
        )
    assert response.status_code == 307
def test_get_employee3():
    response = client.get("/employee")

def test_get_employee4():
    response = client.get("/employee")
def test_get_employee5():
    response = client.get("/employee")
def test_get_employee6():
    response = client.get("/employee")
def test_get_employee7():
    response = client.get("/employee")
def test_get_employee8():
    response = client.get("/employee")
def test_get_employee9():
    response = client.get("/employee")    
def test_get_employee10():
    response = client.get("/employee")
def test_get_employee11():
    response = client.get("/employee")
def test_get_employee12():
    response = client.get("/employee")
def test_get_employee13():
    response = client.get("/employee")
def test_get_employee14():
    response = client.get("/employee")
def test_get_employee15():
    response = client.get("/employee")
def test_get_employee16():
    response = client.get("/employee")
def test_get_employee17():
    response = client.get("/employee")
def test_get_employee18():
    response = client.get("/employee")
def test_get_employee19():
    response = client.get("/employee")
def test_get_employee20():
    response = client.get("/employee")
def test_get_employee21():
    response = client.get("/employee")    
def test_get_employee22():
    response = client.get("/employee")
def test_get_employee23():
    response = client.get("/employee")
def test_get_employee24():
    response = client.get("/employee")
def test_get_employee25():
    response = client.get("/employee")
def test_get_employee26():
    response = client.get("/employee")
def test_get_employee27():
    response = client.get("/employee")        