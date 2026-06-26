# Write a program to Create quiz application
score = 0

print("===== Welcome to the Quiz =====")

# Question 1
print("\nQ1. What is the capital of India?")
print("a) Mumbai")
print("b) Delhi")
print("c) Kolkata")
print("d) Chennai")

answer = input("Enter your answer (a/b/c/d): ").lower()

if answer == "b":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is b) Delhi")

# Question 2
print("\nQ2. Which language is used for Data Science?")
print("a) Python")
print("b) HTML")
print("c) CSS")
print("d) XML")

answer = input("Enter your answer (a/b/c/d): ").lower()

if answer == "a":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is a) Python")

# Question 3
print("\nQ3. 5 + 7 = ?")
print("a) 10")
print("b) 11")
print("c) 12")
print("d) 13")

answer = input("Enter your answer (a/b/c/d): ").lower()

if answer == "c":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is c) 12")

# Final Result
print("\n===== Quiz Finished =====")
print("Your Score:", score, "/ 3")

if score == 3:
    print("Excellent! 🎉")
elif score == 2:
    print("Good Job! 👍")
elif score == 1:
    print("Keep Practicing! 😊")
else:
    print("Better Luck Next Time! 😄")
