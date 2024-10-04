import excel
import contacts
import whatsapp
import quote
from datetime import datetime

today = datetime.now().strftime('%d-%m-%Y')

def sendMessageToDishWasher():
    todaysDishwasher = excel.getTodaysDishWasher()
    
    if todaysDishwasher:
        for contact in contacts.getContacts():
            if contact['name'] == todaysDishwasher:
                whatsapp.sendMessage(contact['phone_number'], f"Beste {contact['name']},\nvandaag heb jij de zwafwastaak.\nVergeet het vuilnis niet😃👍\n\n{quote.getQuote()}\n\nmet vriendelijke groeten,\nHuisbitchBot")
                break
        whatsapp.sendMessageGroup(f"ERROR: {todaysDishwasher} not in contacts:\n {contacts}")

    else:
        whatsapp.sendMessageGroup(f"ERROR: no valid dishwasher today. dishwasher: {todaysDishwasher}")


def sendMessageMondayChores():
    for contact in contacts.getContacts():
        print(excel.getTaskFromContactName(contact['name']))

        contactTask = excel.getTaskFromContactName(contact['name'])
        
        if contactTask:
            print(contact['name'], contactTask, today)

            whatsapp.sendMessage(contact['phone_number'], 
                                 f"""Beste {contact['name']},\n"""
                                 f"""Vandaag is het maandag {today} en dat betekent dat jij je weer in gaat zetten voor een mooi en schoon huize Appa!\n"""
                                 f"""Jouw huistaak van vandaag is {contactTask} zet hem op jij kanjer!\n\n"""
                                 f"""{quote.getQuote()}\n\n"""
                                 f"""Met vriendelijke groeten,\n"""
                                 f"""HuisBitchBot🧹🪣✨\n\n"""
                                 f"""(dit is een test)""", closeTab=True)


def main():
    excel.init()

    if datetime.now().weekday() == 0:
        sendMessageMondayChores()

    sendMessageToDishWasher()

    if excel.errorLog:
        whatsapp.sendMessageGroup(f"ERROR LOG HUISTAKEN:\n\n{excel.errorLog}")

    exit()
        


if __name__ == "__main__":
    main()
