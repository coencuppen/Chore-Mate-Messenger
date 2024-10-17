import pywhatkit
import pyautogui
import time

waiting_time_to_send = 60
waiting_time_to_close = 20

groupId = "HuisbitchBot Error log"

def focus_browser():
    # Pause to ensure page loads
    time.sleep(2)
    # Click on a location where the browser should be (you can adjust the coordinates)
    pyautogui.click(x=500, y=500)

def sendMessage(phoneNumber : str, message : str, closeTab = True):
    try:
        focus_browser()
        pywhatkit.sendwhatmsg_instantly(phoneNumber, message, waiting_time_to_send, closeTab, 2)
    except Exception as e:
        sendMessageGroup(f"ERROR: failed to send message to {phoneNumber} with message:\n{message}\n\n {e}")

def sendMessageGroup(message):
    try:
        focus_browser()
        pywhatkit.sendwhatmsg_to_group_instantly(group_id=groupId, message=message, wait_time=waiting_time_to_send, tab_close=True)
    except Exception as e:
        print(f"failed sendMessageGroup() {e}")