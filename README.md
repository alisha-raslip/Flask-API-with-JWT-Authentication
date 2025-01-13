
# Flask API with JWT Authentication

This project demonstrates the implementation of authentication and security in a Flask application using JSON Web Tokens (JWT). It includes features such as user login, token generation, and validation to secure protected routes and ensure only authenticated users can access them.

## Features

- **User Authentication**: Verifies user credentials and issues a JWT.
- **JWT Token Generation**: Securely encodes user-specific claims (e.g., user ID, expiration).
- **Protected Routes**: Restricts access to specific endpoints using JWT.
- **Error Handling**: Gracefully handles invalid, expired, or missing tokens.

## Authentication Flow

### 1. Login
- Users provide their credentials (username and password).
- On successful authentication, a JWT is issued.

### 2. Token Usage
- The client stores the token and includes it in the `Authorization` header for protected routes.

### 3. Token Validation
- The server validates the token's signature and claims (e.g., expiration).
- If valid, the user is granted access; otherwise, an error is returned.

## API Endpoints

### Public Endpoint

#### `POST /api/login`
Authenticates the user and generates a JWT.

**Request Body**:
```json
{
  "username": "test_user",
  "password": "plain_text_password"
}
```

**Response**:
```json
{
  "token": "<your_jwt_token>"
}
```

---

### Protected Endpoint

#### `GET /api/protected`
Returns data accessible only to authenticated users.

**Headers**:
```text
Authorization: Bearer <your_jwt_token>
```

**Response**:
```json
{
  "message": "You have access to this route",
  "data": {
    "user_id": 1,
    "exp": 1684277200
  }
}
```

---

## Setup and Installation

### Clone the Repository
```bash
git clone <repository-url>
cd <repository-name>
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Set Environment Variables

For **Command Prompt** (Windows):
```bash
set FLASK_APP=app:create_app
set FLASK_ENV=development
```

For **PowerShell** (Windows):
```bash
$env:FLASK_APP="app:create_app"
$env:FLASK_ENV="development"
```

### Run the Application
```bash
flask run
```

### Test the API

You can test the API using **Hoppscotch**.

---

## Testing

### Hoppscotch Configuration

1. Open **Hoppscotch** (https://hoppscotch.io/).
2. Use the `POST /api/login` endpoint to obtain a JWT.
3. Add the token to the `Authorization` header in subsequent requests to access the protected endpoint (`/api/protected`).

---

### Example Requests

#### Login Request
```bash
curl -X POST http://127.0.0.1:5000/api/login \
  -H "Content-Type: application/json" \
  -d '{"username": "test_user", "password": "plain_text_password"}'
```

#### Protected Route Request
```bash
curl -X GET http://127.0.0.1:5000/api/protected \
  -H "Authorization: Bearer <your_jwt_token>"
```

---

## Folder Structure

```
flask-auth/
├── app/
│   ├── __init__.py
│   ├── auth.py
│   ├── routes.py
│   ├── config.py
├── tests/
│   └── test_auth.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Security Considerations

- **JWT Secret Key**: Use a strong, unique `SECRET_KEY` for JWT encoding.
- **User Input Validation**: Always validate user input to prevent injection attacks.
- **HTTPS**: Use HTTPS in production to secure token transmission.
- **Regular Key Rotation**: Regularly rotate secret keys to enhance security.

---

## Dependencies

- **Flask**
- **PyJWT**
- **Flask-Bcrypt**

Install all dependencies using:
```bash
pip install -r requirements.txt
```

---

## Troubleshooting

### Common Issues

- **"Token is missing"**: Ensure the `Authorization` header is included and properly formatted.
- **"Token has expired"**: The token’s `exp` claim has passed; request a new token.
- **"Invalid token"**: Verify that the token matches the one issued by the `/api/login` endpoint.

### Debugging Tips

- Use `print()` statements or Flask debug mode to trace errors.
- Check the Flask application logs for detailed error messages.

---

## Contribution Guidelines

- Follow PEP 8 standards for Python code.
- Write meaningful commit messages.
- Test all endpoints thoroughly before submitting changes.

---

## License

This project is licensed under the MIT License.

---

Let me know if you'd like any more adjustments!