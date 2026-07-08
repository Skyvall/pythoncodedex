

sent_message = "Hello, this is a test message."
unsent_message = "This message has been unsent."

with open("sent_message.txt", "w") as file:
    file.write(sent_message)

with open("sent_message.txt", "r+") as file:
    original_message = file.read()
    print("Original message:", original_message)

    file.seek(0)
    file.write(unsent_message)
    file.truncate()

    file.seek(0)
    updated_message = file.read()
    print("Updated message:", updated_message)
