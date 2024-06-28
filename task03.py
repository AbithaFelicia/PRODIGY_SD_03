import json

CONTACTS_FILE = 'contacts.json'

# Load contacts from the file
def load_contacts():
    try:
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save contacts to the file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")

    contact = {'name': name, 'phone': phone, 'email': email}
    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for idx, contact in enumerate(contacts, start=1):
            print(f"Contact {idx}:")
            print(f"  Name: {contact['name']}")
            print(f"  Phone: {contact['phone']}")
            print(f"  Email: {contact['email']}")
            print("-" * 20)

# Edit an existing contact
def edit_contact(contacts):
    view_contacts(contacts)
    contact_index = int(input("Enter the contact number to edit: ")) - 1

    if 0 <= contact_index < len(contacts):
        contact = contacts[contact_index]
        print("Leave field empty to keep the current value.")
        name = input(f"Enter new name (current: {contact['name']}): ")
        phone = input(f"Enter new phone (current: {contact['phone']}): ")
        email = input(f"Enter new email (current: {contact['email']}): ")

        if name:
            contact['name'] = name
        if phone:
            contact['phone'] = phone
        if email:
            contact['email'] = email

        save_contacts(contacts)
        print("Contact updated successfully!")
    else:
        print("Invalid contact number.")

# Delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    contact_index = int(input("Enter the contact number to delete: ")) - 1

    if 0 <= contact_index < len(contacts):
        contacts.pop(contact_index)
        save_contacts(contacts)
        print("Contact deleted successfully!")
    else:
        print("Invalid contact number.")

# Main function to display the menu and handle user input
def main():
    contacts = load_contacts()
    
    while True:
        print("\nContact Manager")
        print("1. Add a new contact")
        print("2. View contacts")
        print("3. Edit a contact")
        print("4. Delete a contact")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting the Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
