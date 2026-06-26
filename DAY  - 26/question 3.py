#Write a program to Create ATM simulation. 
balance = 10000

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = int(input("enter your choice (1-4) : "))
    if choice == 1:
        print("Your current balance is:", balance)

    elif choice == 2:
        amount = float(input("enter amount to deposit : "))
        if amount > 0:
            balance += amount
            print("Deposit successful.")
            print("Updated Balance:", balance)
        else:
            print("Invalid amount!")

    elif choice == 3:
        amount = float(input("enter amount to withdraw : "))
        if amount <= 0:
            print("Invalid amount!")
        elif amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            print("Withdrawal successful.")
            print("Remaining Balance:", balance)

    elif choice == 4:
        print("Thank you for using the ATM!")
        break

    else:
        print("Invalid choice! Please try again.")
