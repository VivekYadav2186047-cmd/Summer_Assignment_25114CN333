# Write a program to Create salary management 
# system. 
employees = {}

while True:
    print("\n===== Salary Management System =====")
    print("1. Add Employee Salary")
    print("2. View All Salaries")
    print("3. Search Employee Salary")
    print("4. Update Salary")
    print("5. Delete Employee Record")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        emp_id = input("Enter Employee ID: ")

        if emp_id in employees:
            print("Employee already exists!")
        else:
            name = input("Enter Employee Name: ")
            basic = float(input("Enter Basic Salary: "))
            bonus = float(input("Enter Bonus: "))
            deduction = float(input("Enter Deduction: "))

            net_salary = basic + bonus - deduction

            employees[emp_id] = {
                "Name": name,
                "Basic Salary": basic,
                "Bonus": bonus,
                "Deduction": deduction,
                "Net Salary": net_salary
            }

            print("Salary record added successfully!")

    elif choice == "2":
        if len(employees) == 0:
            print("No salary records found.")
        else:
            print("\nSalary Records:")
            for emp_id, details in employees.items():
                print("----------------------------")
                print("Employee ID:", emp_id)
                print("Name:", details["Name"])
                print("Basic Salary:", details["Basic Salary"])
                print("Bonus:", details["Bonus"])
                print("Deduction:", details["Deduction"])
                print("Net Salary:", details["Net Salary"])

    elif choice == "3":
        emp_id = input("Enter Employee ID to search: ")

        if emp_id in employees:
            print("\nEmployee Salary Found")
            print("Employee ID:", emp_id)
            print("Name:", employees[emp_id]["Name"])
            print("Basic Salary:", employees[emp_id]["Basic Salary"])
            print("Bonus:", employees[emp_id]["Bonus"])
            print("Deduction:", employees[emp_id]["Deduction"])
            print("Net Salary:", employees[emp_id]["Net Salary"])
        else:
            print("Employee not found!")

    elif choice == "4":
        emp_id = input("Enter Employee ID to update salary: ")

        if emp_id in employees:
            basic = float(input("Enter New Basic Salary: "))
            bonus = float(input("Enter New Bonus: "))
            deduction = float(input("Enter New Deduction: "))

            employees[emp_id]["Basic Salary"] = basic
            employees[emp_id]["Bonus"] = bonus
            employees[emp_id]["Deduction"] = deduction
            employees[emp_id]["Net Salary"] = basic + bonus - deduction

            print("Salary updated successfully!")
        else:
            print("Employee not found!")

    elif choice == "5":
        emp_id = input("Enter Employee ID to delete: ")

        if emp_id in employees:
            del employees[emp_id]
            print("Employee record deleted successfully!")
        else:
            print("Employee not found!")

    elif choice == "6":
        print("Exiting Salary Management System...")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")
