# Library Management System

library = []

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        book = input("Enter book name: ")
        library.append(book)
        print("Book added successfully!")

    elif choice == "2":
        if len(library) == 0:
            print("Library is empty.")
        else:
            print("\nAvailable Books:")
            for i, book in enumerate(library, start=1):
                print(f"{i}. {book}")

    elif choice == "3":
        search = input("Enter book name to search: ")
        if search in library:
            print("Book found in the library.")
        else:
            print("Book not found.")

    elif choice == "4":
        remove = input("Enter book name to remove: ")
        if remove in library:
            library.remove(remove)
            print("Book removed successfully!")
        else:
            print("Book not found.")

    elif choice == "5":
        print("Thank you for using the Library Management System.")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
