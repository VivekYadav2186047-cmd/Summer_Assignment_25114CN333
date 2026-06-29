# Write a program to Create mini library 
# system.
books = []

while True:
    print("\n===== MINI LIBRARY SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book = input("Enter book name: ")
        books.append(book)
        print("Book added successfully!")

    elif choice == 2:
        if len(books) == 0:
            print("Library is empty!")
        else:
            print("\nBooks in Library:")
            for i, book in enumerate(books, start=1):
                print(i, ".", book)

    elif choice == 3:
        book = input("Enter book name to search: ")
        if book in books:
            print("Book is available in the library.")
        else:
            print("Book not found.")

    elif choice == 4:
        book = input("Enter book name to remove: ")
        if book in books:
            books.remove(book)
            print("Book removed successfully!")
        else:
            print("Book not found.")

    elif choice == 5:
        print("Thank you for using the Mini Library System!")
        break

    else:
        print("Invalid choice! Please try again.")
