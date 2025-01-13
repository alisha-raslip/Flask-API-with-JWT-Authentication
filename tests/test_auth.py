import requests

BASE_URL = "http://127.0.0.1:5000"

def test_login():
    """Test the login endpoint."""
    response = requests.post(f"{BASE_URL}/api/login", json={
        "username": "test_user",
        "password": "plain_text_password"
    })
    print(response.json())

def test_protected_route():
    """Test the protected route with a valid token."""
    login_response = requests.post(f"{BASE_URL}/api/login", json={
        "username": "test_user",
        "password": "plain_text_password"
    })
    token = login_response.json().get('token')
    headers = {"Authorization": token}
    response = requests.get(f"{BASE_URL}/api/protected", headers=headers)
    print(response.json())

if __name__ == "__main__":
    test_login()
    test_protected_route()
