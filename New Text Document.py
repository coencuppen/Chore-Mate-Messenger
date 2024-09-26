import pywhatkit

phone_numer = '+31 6 48511889'
group_id = ''
message = 'Hoi lInnnnn hallo heo gaat het?'
time_hour = 18
time_minute = 00
waiting_time_to_send = 10
close_tab = True
waiting_time_to_close = 10

mode = "contact"

if mode == "contact":
    pywhatkit.sendwhatmsg(phone_numer, message, time_hour, time_minute, waiting_time_to_send, close_tab, waiting_time_to_close)
elif mode == "group":
    pywhatkit.sendwhatmsg_to_group(group_id, message, time_hour, time_minute, waiting_time_to_send, close_tab, waiting_time_to_close)
else:
    print("Error code: 97654")
    print("Error Message: Please select a mode to send your message.")