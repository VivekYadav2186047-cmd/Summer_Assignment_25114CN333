# Write a program to Find maximum occurring 
# character.
text = input("enter a string = ")

max_char = ""
max_count = 0
for ch in text:
    count = text.count(ch)
    if count > max_count:
        max_count = count
        max_char = ch

print("maximum occurring character:", max_char)
print("frequency:", max_count)
