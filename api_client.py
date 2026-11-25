import requests

API_URL = "http://127.0.0.1:8000"
TIMEOUT = 5


def get_operators(skip: int = 0, limit: int = 50):
    params = {"skip": skip, "limit": limit}
    response = requests.get(f"{API_URL}/operators/", params=params, timeout=TIMEOUT)
    response.raise_for_status()
    return response.json()


def get_operator(operator_id: int):
    response = requests.get(f"{API_URL}/operators/{operator_id}", timeout=TIMEOUT)
    if response.status_code == 404:
        return None
    response.raise_for_status()
    return response.json()


def create_operator(payload: dict):
    response = requests.post(f"{API_URL}/operators/", json=payload, timeout=TIMEOUT)
    response.raise_for_status()
    return response.json()


def update_operator(operator_id: int, payload: dict):
    response = requests.put(f"{API_URL}/operators/{operator_id}", json=payload, timeout=TIMEOUT)
    response.raise_for_status()
    return response.json()


def delete_operator(operator_id: int):
    response = requests.delete(f"{API_URL}/operators/{operator_id}", timeout=TIMEOUT)
    response.raise_for_status()
