import json

filePath = "contacts.json"

def get_contacts():
    try:
        with open(filePath, "r") as file:
            data = json.load(file)
            return data.get("contacts", [])  # Return the list of contacts or an empty list if not found
    except FileNotFoundError:
        print(f"Error: The file {filePath} was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from {filePath}.")
        return []

# Example usage of the get_contacts function
def init():
    contacts = get_contacts()

    # Output the contacts
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone Number: {contact['phone_number']}")
