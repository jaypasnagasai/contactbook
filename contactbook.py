Can you write a README GitHub file for this code in MARKDOWN:

import json

# Initialize an empty dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    contacts[name] = {'phone': phone, 'email': email}
    print("Contact added successfully!")

# Function to view all contacts
def view_contacts():
    if contacts:
        print("List of contacts:")
        for name, info in contacts.items():
            print(f"Name: {name}\nPhone: {info['phone']}\nEmail: {info['email']}\n")
    else:
        print("No contacts found.")

# Function to edit an existing contact
def edit_contact():
    name = input("Enter the name of the contact to edit: ")
    if name in contacts:
        print(f"Editing {name}'s information:")
        phone = input(f"Enter the new phone number for {name}: ")
        email = input(f"Enter the new email address for {name}: ")
        contacts[name]['phone'] = phone
        contacts[name]['email'] = email
        print("Contact information updated.")
    else:
        print("Contact not found.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

# Function to save contacts to a JSON file
def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)
    print("Contacts saved successfully.")

# Function to load contacts from a JSON file
def load_contacts():
    global contacts
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
        print("Contacts loaded successfully.")
    except FileNotFoundError:
        print("No contacts file found.")

# Main loop
while True:
    print("\n-- Contact Book --")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Save Contacts")
    print("6. Load Contacts")
    print("7. Exit")
    
    choice = input("Enter your choice (1/2/3/4/5/6/7): ")
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        edit_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        save_contacts()
    elif choice == '6':
        load_contacts()
    elif choice == '7':
        print("Exiting the contact book.")
        break
    else:
        print("Invalid choice. Please choose again.")
