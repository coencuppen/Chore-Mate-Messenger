import pywhatkit


waiting_time_to_send = 10
close_tab = False
waiting_time_to_close = 10

# mode = "contact"

# if mode == "contact":
#     pywhatkit.sendwhatmsg(phone_numer, message, time_hour, time_minute, waiting_time_to_send, close_tab, waiting_time_to_close)
# elif mode == "group":
#     pywhatkit.sendwhatmsg_to_group(group_id, message, time_hour, time_minute, waiting_time_to_send, close_tab, waiting_time_to_close)
# else:
#     print("Error code: 97654")
#     print("Error Message: Please select a mode to send your message.")


def sendMessage(phoneNumber : str, message : str, closeTab = False):
    try:
        pywhatkit.sendwhatmsg_instantly(phoneNumber, message, waiting_time_to_send, closeTab)
    except:
        print("failed")
