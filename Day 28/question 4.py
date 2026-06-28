# Write a program to Create contact 
# management system.


contacts = {}
while True:
    print("\n===== CONTACT MANAGEMENT SYSTEM =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added successfully!")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts available.")
        else:
            print("\n----- Contact List -----")
            for name, phone in contacts.items():
                print("Name:", name, "| Phone:", phone)

    elif choice == "3":
        name = input("Enter contact name to search: ")
        if name in contacts:
            print("Phone Number:", contacts[name])
        else:
            print("Contact not found.")
    elif choice == "4":
        name = input("Enter contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Thank you for using the Contact Management System.")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
