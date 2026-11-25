# Alongside your code to figure out what I needed to do a large portion of this functionality was AI helping me figure out what was going on.
import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


@pytest.fixture
def temp_operator():
    """Creates a temporary operator before a test and deletes it afterward."""
    payload = {
        "OperatorName": "TestOperator",
        "Health": 2,
        "Speed": 2,
        "Difficulty": 1,
        "IsAttacker": True,
    }
    response = client.post("/operators/", json=payload)
    created = response.json()
    yield created

    client.delete(f"/operators/{created['OperatorID']}")

def test_create_operator():
    payload = {
        "OperatorName": "Zero",
        "Health": 2,
        "Speed": 2,
        "Difficulty": 1,
        "IsAttacker": True,
    }
    response = client.post("/operators/", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert data["OperatorName"] == "Zero"
    assert data["Health"] == 2
    assert data["Speed"] == 2
    assert data["Difficulty"] == 1
    assert data["IsAttacker"] is True
    assert "OperatorID" in data

    client.delete(f"/operators/{data['OperatorID']}")

def test_read_all_operators(temp_operator):
    response = client.get("/operators/", params={"limit": 1000})
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert any(op["OperatorID"] == temp_operator["OperatorID"] for op in data)

def test_read_one_operator(temp_operator):
    op_id = temp_operator["OperatorID"]
    response = client.get(f"/operators/{op_id}")
    assert response.status_code == 200

    data = response.json()
    assert data["OperatorID"] == op_id
    assert data["OperatorName"] == temp_operator["OperatorName"]
    assert data["IsDefender"] is False

def test_update_operator(temp_operator):
    op_id = temp_operator["OperatorID"]
    updated_payload = {
        "OperatorName": "UpdatedOperator",
        "Health": 3,
        "Speed": 1,
        "Difficulty": 3,
        "IsAttacker": False,
    }
    response = client.put(f"/operators/{op_id}", json=updated_payload)
    assert response.status_code == 200

    data = response.json()
    assert data["OperatorName"] == "UpdatedOperator"
    assert data["Health"] == 3
    assert data["Speed"] == 1
    assert data["Difficulty"] == 3
    assert data["IsAttacker"] is False

    verify_response = client.get(f"/operators/{op_id}")
    assert verify_response.status_code == 200
    assert verify_response.json()["OperatorName"] == "UpdatedOperator"

def test_delete_operator(temp_operator):
    op_id = temp_operator["OperatorID"]
    response = client.delete(f"/operators/{op_id}")
    assert response.status_code == 200
    assert response.json() == "Operator deleted successfully"

    verify_response = client.get(f"/operators/{op_id}")
    assert verify_response.status_code == 404
