#  Write a program to Develop complete mini 
# project using arrays, strings and functions. 
# Student Record Management System

names = []
roll_numbers = []
courses = []

# Function to add student
def add_student():
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")
    course = input("Enter Course: ")

    names.append(name)
    roll_numbers.append(roll)
    courses.append(course)

    print("Student added successfully!")

# Function to view students
def view_students():
    if len(names) == 0:
        print("No student records found.")
    else:
        print("\n----- Student Records -----")
        print("Roll No\tName\tCourse")
        print("-" * 35)
        for i in range(len(names)):
            print(roll_numbers[i], "\t", names[i], "\t", courses[i])

# Function to search student
def search_student():
    roll = input("Enter Roll Number to Search: ")

    if roll in roll_numbers:
        index = roll_numbers.index(roll)
        print("\nStudent Found")
        print("Name   :", names[index])
        print("Roll   :", roll_numbers[index])
        print("Course :", courses[index])
    else:
        print("Student not found.")

# Function to update student
def update_student():
    roll = input("Enter Roll Number to Update: ")

    if roll in roll_numbers:
        index = roll_numbers.index(roll)

        names[index] = input("Enter New Name: ")
        courses[index] = input("Enter New Course: ")

        print("Record updated successfully!")
    else:
        print("Student not found.")

# Function to delete student
def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    if roll in roll_numbers:
        index = roll_numbers.index(roll)

        names.pop(index)
        roll_numbers.pop(index)
        courses.pop(index)

        print("Record deleted successfully!")
    else:
        print("Student not found.")

# Main Menu
while True:
    print("\n===== STUDENT RECORD MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you! Exiting the program.")
        break

    else:
        print("Invalid choice! Please try again.")
