def add_contact(contact):
    name = input("Enter name: ")
    if name in contact:
        print("already exists")
        return
    phone = input("Enter phone: ")
    mail = input("Enter email: ")
    contact[name] = {"phone": phone, "mail": mail}
    print(f"Contact '{name}' added successfully!")
    pass


def view_contact(contact):
    name = input("Enter name to view contact: ")
    if name not in contact:
        print("Not found")
        return
    else:
        print(contact[name])


def edit_contact(contact):
    name = input("Enter name: ")
    if name not in contact:
        print("Not found")
        return
    print("Reenter all information\n")
    phone = input("Enter phone: ")
    mail = input("Enter email: ")
    c = {"phone": phone, "mail": mail}
    contact[name] = c


def delete_contact(contact):
    name = input("Enter name: ")
    if name not in contact:
        print("Not found")
        return
    del contacts[name]
    print(f"Contact '{name}' deleted successfully!")


contacts = {}

while True:

    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_contact(contacts)
    elif choice == "2":
        view_contact(contacts)
    elif choice == "3":
        edit_contact(contacts)
    elif choice == "4":
        delete_contact(contacts)
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
