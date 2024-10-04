import json

filePath = "contacts.json"

def getContacts():
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

