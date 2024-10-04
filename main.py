import excel
import contacts
import whatsapp
import quote

def main():
    excel.init()
    contacts.init()

    todaysDishwasher = excel.getTodaysDishWasher()
    
    if todaysDishwasher:
        for contact in contacts.getContacts():
            if contact['name'] == todaysDishwasher:
                whatsapp.sendMessage(contact['phone_number'], f"Beste {contact['name']},\nvandaag heb jij de zwafwastaak.\nVergeet het vuilnis niet😃👍\n\n{quote.getQuote()}\n\nmet vriendelijke groeten,\nHuisbitchBot")
                break
        whatsapp.sendMessageGroup(f"ERROR: {todaysDishwasher} not in contacts:\n {contacts}")

    else:
        whatsapp.sendMessageGroup(f"ERROR: no valid dishwasher today. dishwasher: {todaysDishwasher}")


if __name__ == "__main__":
    main()
