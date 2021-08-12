from fastapi.testclient import TestClient
import main 
client = TestClient(main.app)

def test_get_status():
    response = client.get("/BackendStatus")
    assert response.status_code == 200
    assert response.json() == {"status": "running"}

def test_get_employee():
    response = client.get("/employee")
    assert response.status_code == 200
    
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

def test_get_report():
    response = client.get("/report")
    assert response.status_code == 200
    assert {
    "_id": "61152f1dd5b12c96f2d94cde",
    "name": "Report 4",
    "metric": "wellbeing",
    "department": " Fairs, Exhibitions, Events  展会、展览、活动",
    "year": "2021",
    "report_format": "chart",
    "question": "wellbeing",
    "label_x": "Question",
    "label_y": "Mean Score",
    "data_x": [
      "w_1_mean",
      "w_2_mean",
      "w_3_mean",
      "w_4_mean",
      "w_5_mean"
    ],
    "data_y": [
      "4.0",
      "3.0",
      "4.0",
      "4.0",
      "3.0"
    ]
  } in response.json()

def test_get_individuals_report():
    response = client.get("/report/individuals/25443")
    assert response.status_code == 200
    assert response.json() == [
  {
    "_id": "60f13939fe3c44517d367abd",
    "Employee_id": "25443.0",
    "EES_score": "90.39271131152054",
    "Opinion": "100.0",
    "Wellbeing": "82.62812758589709",
    "Core_values": "88.30668560521652",
    "Personality": "89.65614686556853",
    "Flight_risk_label": "Low Flight Risk",
    "year": "2021"
  }
]

def test_get_report_metric():
    response = client.get("/report/wellbeing")
    assert response.status_code == 200
    assert {
    "_id": "61152f1dd5b12c96f2d94cde",
    "name": "Report 4",
    "metric": "wellbeing",
    "department": " Fairs, Exhibitions, Events  展会、展览、活动",
    "year": "2021",
    "report_format": "chart",
    "question": "wellbeing",
    "label_x": "Question",
    "label_y": "Mean Score",
    "data_x": [
      "w_1_mean",
      "w_2_mean",
      "w_3_mean",
      "w_4_mean",
      "w_5_mean"
    ],
    "data_y": [
      "4.0",
      "3.0",
      "4.0",
      "4.0",
      "3.0"
    ]
  } in response.json()

def test_get_individuals_report_by_year():
    response = client.get("/report/individuals/year/2021")
    assert response.status_code == 200
    assert {
    "_id": "60f13939fe3c44517d367abd",
    "Employee_id": "25443.0",
    "EES_score": "90.39271131152054",
    "Opinion": "100.0",
    "Wellbeing": "82.62812758589709",
    "Core_values": "88.30668560521652",
    "Personality": "89.65614686556853",
    "Flight_risk_label": "Low Flight Risk",
    "year": "2021"
  } in response.json()

def test_get_survery_completion_rate():
    response = client.get("/email/completion_rate")
    assert response.status_code == 200
    assert response.json() == [
  0.79
]

def test_get_survery_completion_number():
    response = client.get("/email/completion_number")
    assert response.status_code == 200
    assert response.json() == [
  237
]

def test_get_list_users():
    response = client.get("/user")
    assert response.status_code == 200
    assert response.json() == [{"_id":"60bd9503ad67eeea5451fdaa","name":"Jane Doe","email":"jdoe@example.com","department":"IT","number_employee":11.0},
    {"_id":"60bd9579ad67eeea5451fdab","name":"ucy2","email":"ucy2@example.com","department":"IT","number_employee":11.0},
    {"_id":"60bdb77c4b2ec88180c75d54","name":"Geo","email":"jdoe@example.com","department":"IT","number_employee":11.0}] 

def test_show_user():
    response = client.get("/user/60bd9503ad67eeea5451fdaa")
    assert response.status_code == 200
    assert response.json() == {"_id":"60bd9503ad67eeea5451fdaa","name":"Jane Doe","email":"jdoe@example.com","department":"IT","number_employee":11.0}




