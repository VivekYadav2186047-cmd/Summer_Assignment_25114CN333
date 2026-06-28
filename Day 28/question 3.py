# Write a program to Create ticket booking 
# system.


total_tickets = int(input("enter total number of tickets = "))
available_tickets = total_tickets
while True:
    print("\n===== TICKET BOOKING SYSTEM =====")
    print("1. Book Ticket")
    print("2. Cancel Ticket")
    print("3. Check Available Tickets")
    print("4. Exit")

    choice = input("enter your choice (1-4): ")

    if choice == "1":
        tickets = int(input("enter number of tickets to book = "))
        if tickets <= available_tickets and tickets > 0:
            available_tickets -= tickets
            print("Ticket booked successfully!")
        else:
            print("Sorry! Tickets not available.")
    elif choice == "2":
        tickets = int(input("enter number of tickets to cancel = "))
        if tickets > 0 and available_tickets + tickets <= total_tickets:
            available_tickets += tickets
            print("Ticket cancelled successfully!")
        else:
            print("Invalid cancellation!")

    elif choice == "3":
        print("Available Tickets:", available_tickets)

    elif choice == "4":
        print("Thank you for using the Ticket Booking System.")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
