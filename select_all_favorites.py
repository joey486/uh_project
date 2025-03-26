import uiautomator2 as u2
import time

# Connect to device
d = u2.connect()

# Launch SmartThings app
d.app_start("com.samsung.android.oneconnect")
time.sleep(5)  # Wait for the app to load

print("SmartThings app launched!")

# Wait for elements to appear
d.wait_timeout = 10  # Wait up to 10 seconds for elements to show

# Check if elements exist before interacting
widgets = d(resourceId="com.samsung.android.oneconnect:id/favorite_device_card")

if widgets.exists:
    print(f"Found {len(widgets)} widgets. Clicking them one by one...")

    for widget in widgets:
        if widget.exists:  # Double-check before clicking
            widget.click()
            time.sleep(3)  # Allow time for screen transition
            
            # Dump the new UI hierarchy
            xml_data = d.dump_hierarchy()

            # Save the first widget to an XML file
            with open("first_widget.xml", "w", encoding="utf-8") as file:
                file.write(xml_data)

            print("UI hierarchy saved to first_widget.xml")

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

print("Task completed.")
