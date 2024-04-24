# chat_app.py

class ChatApp:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[name] = number
        print(f"Contact '{name}' added successfully!")

    def send_message(self, recipient, message):
        if recipient in self.contacts:
            print(f"Message sent to {recipient}: {message}")
        else:
            print(f"Recipient '{recipient}' not found in contacts.")

    def show_contacts(self):
        if self.contacts:
            print("Contacts:")
            for name, number in self.contacts.items():
                print(f"{name}: {number}")
        else:
            print("No contacts available.")


def main():
    chat_app = ChatApp()

    while True:
        print("\nSimple Chat Application")
        print("1. Add Contact")
        print("2. Send Message")
        print("3. Show Contacts")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter contact name: ")
            number = input("Enter contact number: ")
            chat_app.add_contact(name, number)

        elif choice == "2":
            recipient = input("Enter recipient's name: ")
            message = input("Enter message: ")
            chat_app.send_message(recipient, message)

        elif choice == "3":
            chat_app.show_contacts()

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
