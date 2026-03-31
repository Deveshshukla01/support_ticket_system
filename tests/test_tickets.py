import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_ticket():
    response = client.post(
        "/tickets",
        json={
            "title": "Test Ticket",
            "description": "Test Description"
        }
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Ticket created successfully"


def test_get_all_tickets():
    response = client.get("/tickets")
    assert response.status_code == 200


def test_get_ticket_by_id():
    response = client.get("/tickets/1")
    assert response.status_code in [200, 404]


def test_update_status():
    response = client.put(
        "/tickets/1/status",
        json={"status": "closed"}
    )
    assert response.status_code in [200, 404]


def test_assign_ticket():
    response = client.put(
        "/tickets/1/assign",
        json={"agent_id": 1}
    )
    assert response.status_code in [200, 404]


def test_delete_ticket():
    response = client.delete("/tickets/1")
    assert response.status_code in [200, 404]