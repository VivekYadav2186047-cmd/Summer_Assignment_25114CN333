# Write a program to Create inventory 
# management system.
inventory = {}

while True:
    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Product Quantity")
    print("4. Delete Product")
    print("5. Search Product")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter product name: ")
        qty = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        inventory[name] = {"Quantity": qty, "Price": price}
        print("Product added successfully!")

    elif choice == 2:
        if len(inventory) == 0:
            print("Inventory is empty.")
        else:
            print("\nProduct\tQuantity\tPrice")
            print("-" * 35)
            for name, details in inventory.items():
                print(f"{name}\t{details['Quantity']}\t\t{details['Price']}")

    elif choice == 3:
        name = input("Enter product name to update: ")
        if name in inventory:
            qty = int(input("Enter new quantity: "))
            inventory[name]["Quantity"] = qty
            print("Quantity updated successfully!")
        else:
            print("Product not found.")

    elif choice == 4:
        name = input("Enter product name to delete: ")
        if name in inventory:
            del inventory[name]
            print("Product deleted successfully!")
        else:
            print("Product not found.")

    elif choice == 5:
        name = input("Enter product name to search: ")
        if name in inventory:
            print("\nProduct Found")
            print("Quantity:", inventory[name]["Quantity"])
            print("Price:", inventory[name]["Price"])
        else:
            print("Product not found.")

    elif choice == 6:
        print("Exiting Inventory Management System...")
        break

    else:
        print("Invalid choice! Please try again.")
