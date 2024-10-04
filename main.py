import excel
import contacts
import whatsapp

def main():
    excel.init()
    contacts.init()

    todaysDishwasher = excel.getTodaysDishWasher()
    
    if todaysDishwasher:
        for contact in contacts.getContacts():
            if contact['name'] == todaysDishwasher:
                whatsapp.sendMessage(contact['phone_number'], f"Beste {contact['name']}, vandaag heb jij de zwafwastaak.\nmet vriendelijke groeten,\nHuisbitchBot")
                continue
        whatsapp.sendMessageGroup(f"ERROR: {todaysDishwasher} not in contacts:\n {contacts}")

    else:
        whatsapp.sendMessageGroup(f"ERROR: no valid dishwasher today. dishwasher: {todaysDishwasher}")


if __name__ == "__main__":
    main()