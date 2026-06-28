# Write a program to Create bank account 
# system.
# Bank Account System

name = input("Enter Account Holder Name: ")
balance = float(input("Enter Initial Balance: "))

while True:
    print("\n===== BANK ACCOUNT SYSTEM =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            print("Amount deposited successfully!")
        else:
            print("Invalid amount!")

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print("Amount withdrawn successfully!")
        else:
            print("Insufficient balance!")

    elif choice == "3":
        print("\n===== ACCOUNT DETAILS =====")
        print("Account Holder:", name)
        print("Current Balance: ₹", balance)

    elif choice == "4":
        print("Thank you for using the Bank Account System.")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
