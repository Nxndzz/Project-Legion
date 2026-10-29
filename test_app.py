import pytest
import app as banking


@pytest.fixture(autouse=True)
def reset_balance():
    banking.balance = 1000.00


@pytest.fixture
def client():
    app = banking.app
    app.config["TESTING"] = True

    with app.test_client() as test_client:
        yield test_client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Simple Banking Application" in response.data


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_balance(client):
    response = client.get("/balance")
    assert response.json["balance"] == 1000.00


def test_deposit(client):
    response = client.post("/deposit", json={"amount": 500})
    assert response.status_code == 200
    assert response.json["balance"] == 1500.00


def test_invalid_deposit(client):
    response = client.post("/deposit", json={"amount": -50})
    assert response.status_code == 400


def test_withdrawal(client):
    response = client.post("/withdraw", json={"amount": 300})
    assert response.status_code == 200
    assert response.json["balance"] == 700.00


def test_insufficient_balance(client):
    response = client.post("/withdraw", json={"amount": 1500})
    assert response.status_code == 400
    assert response.json["message"] == "Insufficient balance"


def test_invalid_withdrawal(client):
    response = client.post("/withdraw", json={"amount": 0})
    assert response.status_code == 400
