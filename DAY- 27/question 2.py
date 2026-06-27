# Write a program to Create employee 
# # management system. 
employees = {}

while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        emp_id = input("Enter Employee ID: ")

        if emp_id in employees:
            print("Employee already exists!")
        else:
            name = input("Enter Employee Name: ")
            age = input("Enter Employee Age: ")
            department = input("Enter Department: ")
            salary = input("Enter Salary: ")

            employees[emp_id] = {
                "Name": name,
                "Age": age,
                "Department": department,
                "Salary": salary
            }

            print("Employee added successfully!")

    elif choice == "2":
        if len(employees) == 0:
            print("No employee records found.")
        else:
            print("\nEmployee Records:")
            for emp_id, details in employees.items():
                print("----------------------------")
                print("Employee ID:", emp_id)
                print("Name:", details["Name"])
                print("Age:", details["Age"])
                print("Department:", details["Department"])
                print("Salary:", details["Salary"])

    elif choice == "3":
        emp_id = input("Enter Employee ID to search: ")

        if emp_id in employees:
            print("\nEmployee Found")
            print("Employee ID:", emp_id)
            print("Name:", employees[emp_id]["Name"])
            print("Age:", employees[emp_id]["Age"])
            print("Department:", employees[emp_id]["Department"])
            print("Salary:", employees[emp_id]["Salary"])
        else:
            print("Employee not found!")

    elif choice == "4":
        emp_id = input("Enter Employee ID to update: ")

        if emp_id in employees:
            employees[emp_id]["Name"] = input("Enter New Name: ")
            employees[emp_id]["Age"] = input("Enter New Age: ")
            employees[emp_id]["Department"] = input("Enter New Department: ")
            employees[emp_id]["Salary"] = input("Enter New Salary: ")

            print("Employee record updated successfully!")
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
        print("Exiting Employee Management System...")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")
