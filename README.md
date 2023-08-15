# Contact Book

This is a simple command-line contact book application written in Python. It allows you to manage and organize your contacts by performing various operations such as adding, viewing, editing, and deleting contacts. Contacts are stored in a JSON file for persistent storage.

## Features

- Add a new contact with a name, phone number, and email address.
- View a list of all saved contacts with their details.
- Edit an existing contact's phone number and email address.
- Delete a contact from the list.
- Save contacts to a JSON file for future use.
- Load previously saved contacts from a JSON file.

## Getting Started

To use the contact book application, follow these steps:

1. Clone this repository to your local machine.
2. Open a terminal and navigate to the repository directory.

## Usage

Run the script using the following command:

```bash
python contact_book.py
```

Once the script is running, you'll be presented with a menu of options. Enter the corresponding number for the action you'd like to perform.

1. Add Contact: Enter the contact's name, phone number, and email address to add a new contact to the list.
2. View Contacts: View a list of all saved contacts along with their details.
3. Edit Contact: Edit an existing contact's phone number and email address.
4. Delete Contact: Remove a contact from the list.
5. Save Contacts: Save the current list of contacts to a JSON file for future use.
6. Load Contacts: Load previously saved contacts from a JSON file.
7. Exit: Quit the contact book application.

## Notes

1. Contacts are stored in a JSON file named "contacts.json" in the same directory as the script.
2. If the "contacts.json" file doesn't exist when attempting to load contacts, a message will be displayed indicating no contacts file was found.

## Contributing

This project is open for contributions. If you find any bugs or have suggestions for improvements, feel free to create an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
