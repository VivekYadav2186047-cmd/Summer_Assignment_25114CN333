# Write a program to Create menu-driven 
# string operations system.
string = ""

while True:
    print("\n===== STRING OPERATIONS MENU =====")
    print("1. Enter String")
    print("2. Display String")
    print("3. Convert to Uppercase")
    print("4. Convert to Lowercase")
    print("5. Reverse String")
    print("6. Find String Length")
    print("7. Count Vowels")
    print("8. Check Palindrome")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        string = input("Enter a string: ")
        print("String stored successfully!")

    elif choice == 2:
        print("String:", string)

    elif choice == 3:
        print("Uppercase:", string.upper())

    elif choice == 4:
        print("Lowercase:", string.lower())

    elif choice == 5:
        print("Reversed String:", string[::-1])

    elif choice == 6:
        print("Length of String:", len(string))

    elif choice == 7:
        count = 0
        for ch in string.lower():
            if ch in "aeiou":
                count += 1
        print("Number of vowels:", count)

    elif choice == 8:
        if string == string[::-1]:
            print("The string is a Palindrome.")
        else:
            print("The string is not a Palindrome.")

    elif choice == 9:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
