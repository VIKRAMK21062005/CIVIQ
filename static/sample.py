import requests

url = "http://127.0.0.1:8000/auth/login"
# Note: 'data=' is for form-data, 'json=' is for JSON
payload = {
    "username": "test1@civiq.com",
    "password": "password123"
}

response = requests.post(url, data=payload)
print(response.json())