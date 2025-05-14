from fastapi.testclient import TestClient
import pytest
from app.main import app, db

client = TestClient(app)


@pytest.fixture(autouse=True)
def clear_db():
    """Clear the database before each test"""
    db.clear()
    yield
    db.clear()


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert "Welcome" in response.json()["message"]


def test_get_items_empty():
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == []


def test_create_and_get_item():
    # Create an item
    test_item = {"name": "Test Item", "description": "This is a test item"}
    response = client.post("/items", json=test_item)
    assert response.status_code == 201
    created_item = response.json()
    assert created_item["name"] == test_item["name"]
    assert created_item["description"] == test_item["description"]
    assert "id" in created_item
    
    # Get all items
    response = client.get("/items")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["id"] == created_item["id"]
    
    # Get specific item
    response = client.get(f"/items/{created_item['id']}")
    assert response.status_code == 200
    assert response.json() == created_item


def test_get_item_not_found():
    response = client.get("/items/nonexistent-id")
    assert response.status_code == 404
    assert "detail" in response.json()
    assert response.json()["detail"] == "Item not found" 