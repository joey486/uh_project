import sys
import json

# Set the default encoding for stdout to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# Load the JSON file
with open('smartthings_devices.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Function to decode Unicode escape sequences
def decode_unicode(data):
    if isinstance(data, str):
        return bytes(data, "utf-8").decode("unicode_escape")
    elif isinstance(data, dict):
        return {key: decode_unicode(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [decode_unicode(item) for item in data]
    return data

# Decode the entire data structure
decoded_data = decode_unicode(data)

# Now `decoded_data` will have both English and decoded Unicode content
# For example, if you want to print the names and locations:
for device in decoded_data:
    print(f"Device Name: {device['name']}")
    print(f"Location: {device['location']}")
    print('-' * 30)

# You can also save the decoded data to a new file if needed
with open('decoded_smartthings_devices.json', 'w', encoding='utf-8') as f:
    json.dump(decoded_data, f, indent=4, ensure_ascii=False)

print("Data extraction and decoding completed.")
