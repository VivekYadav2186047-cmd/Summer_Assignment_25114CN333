# Write a program to Create menu-driven array 
# operations system. 
arr = []

while True:
    print("\n===== MENU =====")
    print("1. Create Array")
    print("2. Display Array")
    print("3. Insert Element")
    print("4. Delete Element")
    print("5. Search Element")
    print("6. Find Maximum Element")
    print("7. Find Minimum Element")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter number of elements: "))
        arr = []
        for i in range(n):
            element = int(input(f"Enter element {i + 1}: "))
            arr.append(element)
        print("Array created successfully!")

    elif choice == 2:
        if len(arr) == 0:
            print("Array is empty!")
        else:
            print("Array:", arr)

    elif choice == 3:
        element = int(input("Enter element to insert: "))
        position = int(input("Enter position (0 to {}): ".format(len(arr))))
        if 0 <= position <= len(arr):
            arr.insert(position, element)
            print("Element inserted successfully!")
        else:
            print("Invalid position!")

    elif choice == 4:
        element = int(input("Enter element to delete: "))
        if element in arr:
            arr.remove(element)
            print("Element deleted successfully!")
        else:
            print("Element not found!")

    elif choice == 5:
        element = int(input("Enter element to search: "))
        if element in arr:
            print("Element found at index", arr.index(element))
        else:
            print("Element not found!")

    elif choice == 6:
        if len(arr) == 0:
            print("Array is empty!")
        else:
            print("Maximum element:", max(arr))

    elif choice == 7:
        if len(arr) == 0:
            print("Array is empty!")
        else:
            print("Minimum element:", min(arr))

    elif choice == 8:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
