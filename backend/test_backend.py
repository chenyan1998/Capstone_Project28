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
def test_get_employee4():
    response = client.get("/employee")