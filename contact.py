import tkinter as tk
from tkinter import messagebox, simpledialog

class Contact:

    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        return self.contacts

    def search_contact(self, search_term):
        return [contact for contact in self.contacts if
                search_term.lower() in contact.name.lower() or search_term in contact.phone]

    def update_contact(self, index, contact):
        self.contacts[index] = contact

    def delete_contact(self, index):
        del self.contacts[index]

class ContactBookApp:

    def __init__(self, master):
        self.master = master
        master.title("Contact Book")

        self.contact_book = ContactBook()

        # Labels and Buttons
        self.label = tk.Label(master, text="Contact Book", font=("Arial", 16))
        self.label.pack(pady=10)

        self.add_button = tk.Button(master, text="Add Contact", command=self.add_contact, font=("Arial", 12))
        self.add_button.pack(pady=5)

        self.view_button = tk.Button(master, text="View Contacts", command=self.view_contacts, font=("Arial", 12))
        self.view_button.pack(pady=5)

        self.search_button = tk.Button(master, text="Search Contact", command=self.search_contact, font=("Arial", 12))
        self.search_button.pack(pady=5)

        self.update_button = tk.Button(master, text="Update Contact", command=self.update_contact, font=("Arial", 12))
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(master, text="Delete Contact", command=self.delete_contact, font=("Arial", 12))
        self.delete_button.pack(pady=5)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter contact name:")
        if not name:
            return
        phone = simpledialog.askstring("Input", "Enter phone number:")
        if not phone:
            return
        email = simpledialog.askstring("Input", "Enter email:")
        if not email:
            return
        address = simpledialog.askstring("Input", "Enter address:")
        if not address:
            return

        contact = Contact(name, phone, email, address)
        self.contact_book.add_contact(contact)
        messagebox.showinfo("Success", "Contact added successfully!")

    def view_contacts(self):
        """Display all contacts in a message box."""
        contacts = self.contact_book.view_contacts()
        if not contacts:
            messagebox.showinfo("Contact List", "No contacts available.")
            return

        contact_list = "\n".join([f"{i + 1}. {contact.name} - {contact.phone}" for i, contact in enumerate(contacts)])
        messagebox.showinfo("Contact List", contact_list)

    def search_contact(self):
        search_term = simpledialog.askstring("Search", "Enter name or phone number to search:")
        if not search_term:
            return

        results = self.contact_book.search_contact(search_term)
        if not results:
            messagebox.showinfo("Search Results", "No contacts found.")
            return

        result_list = "\n".join([f"{contact.name} - {contact.phone}" for contact in results])
        messagebox.showinfo("Search Results", result_list)

    def update_contact(self):
        """Prompt user for contact index and new details to update."""
        index = simpledialog.askinteger("Update", "Enter the contact number to update:")
        if index is None or index < 1 or index > len(self.contact_book.contacts):
            messagebox.showerror("Error", "Invalid contact number.")
            return

        contact = self.contact_book.contacts[index - 1]
        name = simpledialog.askstring("Update Name",
                                      f"Current name: {contact.name}\nEnter new name (leave blank to keep current):")
        phone = simpledialog.askstring("Update Phone",
                                       f"Current phone: {contact.phone}\nEnter new phone (leave blank to keep current):")
        email = simpledialog.askstring("Update Email",
                                       f"Current email: {contact.email}\nEnter new email (leave blank to keep current):")
        address = simpledialog.askstring("Update Address",
                                         f"Current address: {contact.address}\nEnter new address (leave blank to keep current):")
        if name:
            contact.name = name
        if phone:
            contact.phone = phone
        if email:
            contact.email = email
        if address:
            contact.address = address

        messagebox.showinfo("Success", "Contact updated successfully!")

    def delete_contact(self):
        index = simpledialog.askinteger("Delete", "Enter the contact number to delete:")
        if index is None or index < 1 or index > len(self.contact_book.contacts):
            messagebox.showerror("Error", "Invalid contact number.")
            return

        self.contact_book.delete_contact(index - 1)
        messagebox.showinfo("Success", "Contact deleted successfully!")


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
