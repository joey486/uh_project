import uiautomator2 as u2
import time

# Connect to the device
d = u2.connect()

# Launch SmartThings app
d.app_start("com.samsung.android.oneconnect")
time.sleep(5)  # Wait for the app to load

print("SmartThings app launched!")

# Wait for elements to appear
d.wait_timeout = 10  # Wait up to 10 seconds

# Data storage for text file
clicked_widgets = []

# Find all favorite device cards
widgets = d(resourceId="com.samsung.android.oneconnect:id/favorite_device_card")

if widgets.exists:
    print(f"Found {len(widgets)} widgets. Clicking them one by one...")

    for index, widget in enumerate(widgets):
        if widget.exists:  # Ensure it still exists before clicking
            print(f"Clicking widget {index}...")
            widget.click()
            time.sleep(5)  # Allow time for the screen transition

            # Log index
            clicked_widgets.append(f"Index: {index}\n")

            # Find and click the "הצג מפה" button
            map_button = d(text="הצג מפה", className="android.widget.Button")
            time.sleep(3)

            if map_button.exists:
                print("Found button. Clicking it now...")
                map_button.click()
                time.sleep(2)  # Allow time for action to complete
                d.press("back")
            else:
                print("Button not found on this screen.")

            # Return to the previous screen
            d.press("back")
            time.sleep(2)  # Wait before interacting again
else:
    print("No widgets found. Trying to scroll down...")

    # Scroll and retry
    for _ in range(3):  # Try scrolling a few times
        d(scrollable=True).scroll(steps=10)
        time.sleep(2)
        widgets = d(resourceId="com.samsung.android.oneconnect:id/favorite_device_card")

        if widgets.exists:
            print(f"Found {len(widgets)} widgets after scrolling!")
            break
    else:
        print("Still no widgets found. Exiting.")

# Save data to a text file
with open("widget_log.txt", "w", encoding="utf-8") as file:
    file.writelines(clicked_widgets)

print("Task completed. Data saved to widget_log.txt.")
