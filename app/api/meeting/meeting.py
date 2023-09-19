import requests
import json

API_KEY = "videolify_default_secret"
# VIDEOLIFY_URL = "http://localhost:3000/api/v1/meeting"
# VIDEOLIFY_URL = "https://videocall.shivrajan.com/api/v1/meeting"
VIDEOLIFY_URL = "https://videolify.cleverapps.io/api/v1/meeting"

headers = {
    "authorization": API_KEY,
    "Content-Type": "application/json",
}

response = requests.post(
    VIDEOLIFY_URL,
    headers=headers
)

print("Status code:", response.status_code)
data = json.loads(response.text)
print("meeting:", data["meeting"])
