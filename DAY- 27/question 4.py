# Write a program to Create marksheet 
# generation system.
while True:
    print("\n===== Marksheet Generation System =====")
    print("1. Generate Marksheet")
    print("2. Exit")

    choice = input("Enter your choice (1-2): ")

    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")

        sub1 = float(input("Enter marks of Subject 1: "))
        sub2 = float(input("Enter marks of Subject 2: "))
        sub3 = float(input("Enter marks of Subject 3: "))
        sub4 = float(input("Enter marks of Subject 4: "))
        sub5 = float(input("Enter marks of Subject 5: "))

        total = sub1 + sub2 + sub3 + sub4 + sub5
        percentage = total / 5

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 40:
            grade = "D"
        else:
            grade = "F"

        if sub1 >= 40 and sub2 >= 40 and sub3 >= 40 and sub4 >= 40 and sub5 >= 40:
            result = "PASS"
        else:
            result = "FAIL"

        print("\n========== MARKSHEET ==========")
        print("Roll Number :", roll)
        print("Student Name:", name)
        print("--------------------------------")
        print("Subject 1 :", sub1)
        print("Subject 2 :", sub2)
        print("Subject 3 :", sub3)
        print("Subject 4 :", sub4)
        print("Subject 5 :", sub5)
        print("--------------------------------")
        print("Total Marks :", total, "/500")
        print("Percentage  :", round(percentage, 2), "%")
        print("Grade       :", grade)
        print("Result      :", result)
        print("===============================")

    elif choice == "2":
        print("Exiting Marksheet Generation System...")
        break

    else:
        print("Invalid choice! Please enter 1 or 2.")
