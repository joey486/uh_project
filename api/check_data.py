import requests

SMARTTHINGS_TOKEN = "d1f31ec6-331d-4c5d-bb5c-c3544e4b2c4b"
BASE_URL = "https://api.smartthings.com/v1"

HEADERS = {
    "Authorization": f"Bearer {SMARTTHINGS_TOKEN}",
    "Accept": "application/json"
}

def get_device_status(device_id):
    """Fetch device status (instead of capabilities) to check for location data."""
    url = f"{BASE_URL}/devices/{device_id}/status"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching status for {device_id}: {response.status_code}")
        return None

# Get all devices
response = requests.get(f"{BASE_URL}/devices", headers=HEADERS)
devices = response.json().get("items", [])

for device in devices:
    print(f"Checking {device['label']} ({device['deviceId']})...")
    status = get_device_status(device["deviceId"])
    if status:
        print(f"Status: {status}")


def refresh_device(device_id):
    url = f"{BASE_URL}/devices/{device_id}/commands"
    payload = {
        "commands": [{
            "component": "main",
            "capability": "refresh",
            "command": "refresh"
        }]
    }
    response = requests.post(url, json=payload, headers=HEADERS)
    if response.status_code == 200:
        print(f"Refresh command sent to {device_id}")
    else:
        print(f"Error refreshing device {device_id}: {response.status_code}")

# Try refreshing each device
for device in devices:
    refresh_device(device["deviceId"])
