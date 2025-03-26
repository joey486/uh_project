import uiautomator2 as u2
import time

# Connect to the device (Make sure ADB is enabled and the device is connected)
d = u2.connect()

# Launch the SmartThings app
d.app_start("com.samsung.android.oneconnect")
print("SmartThings app launched!")

# Wait for the app to load
time.sleep(5)

# Find and click the favorite device card
favorite_device = d(resourceId="com.samsung.android.oneconnect:id/favorite_device_card")
if favorite_device.exists:
    favorite_device.click()
    print("Favorite device card clicked!")
else:
    print("Favorite device card not found.")

# Optional: Keep the script running for debugging
# time.sleep(10)
