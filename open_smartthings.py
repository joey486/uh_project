import os

# Command to launch SmartThings app
command = "adb shell am start -n com.samsung.android.oneconnect/.ui.SCMainActivity"

# Execute the command
os.system(command)
