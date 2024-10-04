import pywhatkit

waiting_time_to_send = 25
waiting_time_to_close = 5

groupId = "HuisbitchBot Error log"

def sendMessage(phoneNumber : str, message : str, closeTab = True):
    try:
        pywhatkit.sendwhatmsg_instantly(phoneNumber, message, waiting_time_to_send, closeTab)
    except:
        sendMessageGroup(f"ERROR: failed to send message to {phoneNumber} with message:\n{message}")

def sendMessageGroup(message):
    try:
        pywhatkit.sendwhatmsg_to_group_instantly(group_id=groupId, message=message, wait_time=waiting_time_to_send, tab_close=True
                                                 )
    except:
        print("failed sendMessageGroup()")