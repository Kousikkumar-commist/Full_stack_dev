# chat_app_gui.py

import tkinter as tk
from tkinter import messagebox

class ChatAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Chat Application")

        # Dictionary to hold contacts
        self.contacts = {}

        # Create frames
        self.frame_contacts = tk.Frame(root)
        self.frame_contacts.grid(row=0, column=0, padx=10, pady=10)

        self.frame_messages = tk.Frame(root)
        self.frame_messages.grid(row=0, column=1, padx=10, pady=10)

        # Contacts Listbox
        self.contacts_listbox = tk.Listbox(self.frame_contacts, width=30)
        self.contacts_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Messages Text Widget
        self.messages_text = tk.Text(self.frame_messages, height=20, width=50)
        self.messages_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add Contact Entry and Button
        self.add_contact_entry = tk.Entry(self.frame_contacts)
        self.add_contact_entry.pack(side=tk.LEFT, padx=5)
        self.add_contact_button = tk.Button(self.frame_contacts, text="Add Contact", command=self.add_contact)
        self.add_contact_button.pack(side=tk.LEFT)

        # Send Message Entry and Button
        self.send_message_entry = tk.Entry(self.frame_messages)
        self.send_message_entry.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)
        self.send_message_button = tk.Button(self.frame_messages, text="Send", command=self.send_message)
        self.send_message_button.pack(side=tk.BOTTOM)

        # Populate Contacts Listbox
        self.update_contacts_listbox()

    def add_contact(self):
        name = self.add_contact_entry.get()
        if name:
            self.contacts[name] = ""
            self.update_contacts_listbox()
            self.add_contact_entry.delete(0, tk.END)
            messagebox.showinfo("Success", f"Contact '{name}' added successfully!")
        else:
            messagebox.showwarning("Warning", "Please enter a contact name.")

    def send_message(self):
        recipient = self.contacts_listbox.get(tk.ACTIVE)
        message = self.send_message_entry.get()
        if recipient and message:
            messagebox.showinfo("Message Sent", f"Message sent to {recipient}: {message}")
            self.messages_text.insert(tk.END, f"\n{recipient}: {message}")
            self.send_message_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please select a recipient and enter a message.")

    def update_contacts_listbox(self):
        self.contacts_listbox.delete(0, tk.END)
        for name in self.contacts.keys():
            self.contacts_listbox.insert(tk.END, name)


def main():
    root = tk.Tk()
    app = ChatAppGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()