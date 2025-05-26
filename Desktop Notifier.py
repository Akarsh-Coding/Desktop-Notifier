from plyer import notification
import time

def send_notification(title, message, timeout=5):
    """Send a desktop notification using plyer."""
    notification.notify(
        title=title,
        message=message,
        timeout=timeout
    )

if __name__ == "__main__":
    # Settings for notification
    notification_title = "💡 Take a Break!"
    notification_message = "It's time to rest your eyes and stretch your body for better health."
    
    # Set break reminder intervals (e.g., every 20 minutes)
    minute = int(input("Enter the interval time in minute:- "))
    reminder_interval = minute * 60  # Convert minutes to seconds
    
    while True:
        try:
            send_notification(notification_title, notification_message)         # Send the notification
            time.sleep(reminder_interval)       # Pause the script for the set interval before sending the next notification
        except Exception as e:
            print(f"Error occurred: {e}")
            break



# 💡 How to run this program in the background (Windows):
# 1. Save this file as "Desktop Notifier.py"
# 2. Move or save this script inside the Python installation folder 
#    (e.g., C:\Users\<YourName>\AppData\Local\Programs\Python\Python311)
#    OR be sure to reference the full path to pythonw.exe when running it.
# 3. Open the script’s folder in Terminal or PowerShell
# 4. Optional: Run the terminal as Administrator
# 5. Run the script using the following command:
#    > pythonw "Desktop Notifier.py"
#    OR if you're not in the Python folder, use the full path:
#    > "C:\Path\To\pythonw.exe" "C:\Path\To\Desktop Notifier.py"
# ✅ This will run the script silently in the background with no terminal window.

