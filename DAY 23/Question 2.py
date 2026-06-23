
#Write a program to Find first repeating character.
text = input("enter a string =  ")

seen = []
for ch in text:
    if ch in seen:
        print("First repeating character:", ch)
        break
    seen.append(ch)
else:
    print("No repeating character found.")#
