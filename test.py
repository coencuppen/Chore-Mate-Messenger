from wa_automate_socket_client import SocketClient

NUMBER = '+31 6 53900074'

client = SocketClient('http://localhost:8085/', 'secure_api_key')


def printResponse(message):
    print(message)


# Listening for events
client.onMessage(printResponse)

# Executing commands
client.sendText(NUMBER, "this is a text")

# Sync/Async support
print(client.getHostNumber())  # Sync request
client.sendAudio(NUMBER,
                 "https://download.samplelib.com/mp3/sample-3s.mp3",
                 sync=False,
                 callback=printResponse)  # Async request. Callback is optional

# Finally disconnect
client.disconnect()