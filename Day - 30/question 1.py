

# Student Record System using Arrays and Strings

names = []
roll_numbers = []
courses = []

while True:
    print("\n===== STUDENT RECORD SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("enter your choice: "))
    if choice == 1:
        name = input("enter student name: ")
        roll = input("enter roll number: ")
        course = input("enter course: ")

        names.append(name)
        roll_numbers.append(roll)
        courses.append(course)

        print("Student record added successfully!")

    elif choice == 2:
        if len(names) == 0:
            print("No student records found.")
        else:
            print("\nStudent Records:")
            print("Roll No\tName\tCourse")
            print("-" * 30)
            for i in range(len(names)):
                print(roll_numbers[i], "\t", names[i], "\t", courses[i])

    elif choice == 3:
        roll = input("Enter roll number to search: ")

        
        if roll in roll_numbers:
            index = roll_numbers.index(roll)
            print("\nStudent Found")
            print("Name :", names[index])
            print("Roll :", roll_numbers[index])
            print("Course :", courses[index])
        else:
            print("Student not found.")

    elif choice == 4:
        roll = input("Enter roll number to delete: ")

        if roll in roll_numbers:
            index = roll_numbers.index(roll)

            names.pop(index)
            roll_numbers.pop(index)
            courses.pop(index)

            print("Student record deleted successfully!")
        else:
            print("Student not found.")

    elif choice == 5:
        print("Exiting Student Record System...")
        break

    else:
        print("Invalid choice! Please try again.")
