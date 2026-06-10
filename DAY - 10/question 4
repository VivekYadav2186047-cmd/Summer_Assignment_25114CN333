# Write a program to Print character 
#     A 
#    ABA 
#   ABCBA 
#  ABCDCBA 
# ABCDEDCBA
# Print Character Pyramid using While Loop

n = int(input("enter number of rows = "))
i = 1
while i <= n:
    #Print spaces
    space = 1
    while space <= n -i:
        print(" ", end="")
        space += 1

    #increasing characters
    j = 1
    while j <= i:
        print(chr(64 + j), end="")
        j += 1

    #decreasing characters
    j = i -1
    while j >= 1:
        print(chr(64 + j), end="")
        j -= 1

    print()
    i += 1
