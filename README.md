# SmartThings UI Automator Script

## Overview
This Python script automates interactions with the Samsung SmartThings app using `uiautomator2`. It detects and interacts with favorite device cards, clicks through them, attempts to access a specific button labeled in Hebrew ("הצג מפה"), and logs interactions into an Excel file.

## Prerequisites
Before running the script, ensure you have the following installed:

- Python 3.x
- Required Python packages:
  ```bash
  pip install uiautomator2 pandas openpyxl
  ```
- A connected Android device with USB debugging enabled
- The `uiautomator2` daemon installed on the Android device:
  ```bash
  python -m uiautomator2 init
  ```
- The Samsung SmartThings app installed on the device

## How It Works
1. Connects to an Android device via `uiautomator2`.
2. Launches the SmartThings app.
3. Searches for favorite device cards and interacts with them.
4. Attempts to click a button labeled "הצג מפה" if available.
5. Logs clicked widgets into an Excel file (`widget_log.xlsx`).
6. Scrolls down if no widgets are initially found and retries.
7. Saves all interaction data into an Excel file.

## Running the Script
Run the script using:
```bash
python script.py
```

## Expected Output
- The script will output logs in the console indicating the steps performed.
- If widgets are found and interacted with, an Excel file (`widget_log.xlsx`) will be created with the index of clicked widgets.

## Notes
- Ensure your device is unlocked and connected.
- The script uses time delays to allow screen transitions.
- Hebrew text in the script (`הצג מפה`) should match the button label in your app.

## Troubleshooting
- If the device does not connect, restart `uiautomator2` on the device:
  ```bash
  python -m uiautomator2 init
  ```
- If the button is not found, verify its text and class name using:
  ```python
  d.dump_hierarchy()
  ```
  to inspect the UI structure.

## License
This script is provided as-is for automation purposes. Modify as needed to fit your requirements.

