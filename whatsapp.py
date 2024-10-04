import pywhatkit


waiting_time_to_send = 25
close_tab = False
waiting_time_to_close = 10

groupId = "HuisbitchBot Error log"

# mode = "contact"

# if mode == "contact":
#     pywhatkit.sendwhatmsg(phone_numer, message, time_hour, time_minute, waiting_time_to_send, close_tab, waiting_time_to_close)
# elif mode == "group":
#     pywhatkit.sendwhatmsg_to_group(group_id, message, time_hour, time_minute, waiting_time_to_send, close_tab, waiting_time_to_close)
# else:
#     print("Error code: 97654")
#     print("Error Message: Please select a mode to send your message.")


def sendMessage(phoneNumber : str, message : str, closeTab = True):
    try:
        pywhatkit.sendwhatmsg_instantly(phoneNumber, message, waiting_time_to_send, closeTab)
    except:
        sendMessageGroup(f"ERROR: failed to send message to {phoneNumber} with message:\n{message}")

def sendMessageGroup(message):
    try:
        pywhatkit.sendwhatmsg_to_group_instantly(group_id=groupId, message=message, wait_time=waiting_time_to_send, tab_close=True)
    except:
        print("failed sendMessageGroup()")