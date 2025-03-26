import requests

# Replace with your SmartThings OAuth token
oauth_token = 'd1f31ec6-331d-4c5d-bb5c-c3544e4b2c4b'
BASE_URL = "https://api.smartthings.com/v1"

HEADERS = {
    "Authorization": f"Bearer {oauth_token}",
    "Accept": "application/json"
}

def get_devices():
    """Fetch all devices linked to SmartThings."""
    response = requests.get(f"{BASE_URL}/devices", headers=HEADERS)
    if response.status_code == 200:
        return response.json().get("items", [])
    else:
        print(f"Error: {response.status_code}")
        return []

devices = get_devices()

# Display basic device info
for device in devices:
    print(f"Device: {device['label']} (ID: {device['deviceId']})")

# If location is available, extract it
for device in devices:
    # Try to fetch location attributes (some devices might not have them)
    capabilities_url = f"{BASE_URL}/devices/{device['deviceId']}/status"
    response = requests.get(capabilities_url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        # Look for location-based attributes (presence sensors, mobile presence)
        if "latitude" in data or "longitude" in data:
            lat = data["latitude"]
            lon = data["longitude"]
            print(f"{device['label']} is at {lat}, {lon}")
