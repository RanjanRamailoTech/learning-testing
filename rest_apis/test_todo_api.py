import requests


ENDPOINT = "https://todo.pixegami.io/"


def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    
    assert response.status_code == 200
    

def test_can_create_task():
    payload = {
        "content": "my test todo",
        "user_id": "test_user",
        "is_done": False
    }
    
    response = requests.put(ENDPOINT + "/create-task", json=payload)
    
    assert response.status_code == 200
    

def test_can_create_task():
    payload = {
        "content": "my test todo",
        "user_id": "test_user",
        "is_done": False
    }
    
    create_task_response = requests.put(ENDPOINT + "/create-task", json=payload)
    
    
    assert create_task_response.status_code == 200
    
    data = create_task_response.json()
    task_id = data['task']["task_id"]
    
    get_task_response = requests.get(ENDPOINT + f"/get-task/{task_id}")
    
    assert get_task_response.status_code == 200
    
    #its a bad pracice to directly manipulate the database during testing. You might wanna use mocking