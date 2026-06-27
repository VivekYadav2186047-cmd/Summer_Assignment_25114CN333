#Write a program to Create student record 
# management system. 
students = {}

while True:
    print("\n===== Student Record Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        roll = input("Enter Roll Number: ")

        if roll in students:
            print("Student already exists!")
        else:
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            course = input("Enter Course: ")

            students[roll] = {
                "Name": name,
                "Age": age,
                "Course": course
            }

            print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No student records found.")
        else:
            print("\nStudent Records:")
            for roll, details in students.items():
                print("----------------------------")
                print("Roll Number:", roll)
                print("Name:", details["Name"])
                print("Age:", details["Age"])
                print("Course:", details["Course"])

    elif choice == "3":
        roll = input("Enter Roll Number to search: ")

        if roll in students:
            print("\nStudent Found")
            print("Roll Number:", roll)
            print("Name:", students[roll]["Name"])
            print("Age:", students[roll]["Age"])
            print("Course:", students[roll]["Course"])
        else:
            print("Student not found!")

    elif choice == "4":
        roll = input("Enter Roll Number to update: ")

        if roll in students:
            students[roll]["Name"] = input("Enter New Name: ")
            students[roll]["Age"] = input("Enter New Age: ")
            students[roll]["Course"] = input("Enter New Course: ")
            print("Student record updated successfully!")
        else:
            print("Student not found!")

    elif choice == "5":
        roll = input("Enter Roll Number to delete: ")

        if roll in students:
            del students[roll]
            print("Student record deleted successfully!")
        else:
            print("Student not found!")

    elif choice == "6":
        print("Exiting Student Record Management System...")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")
