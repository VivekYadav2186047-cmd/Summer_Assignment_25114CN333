#Write a program to Compress a string.
def compress_string(s):
    compressed = ""
    count = 1

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
        else:
            compressed += s[i] + str(count)
            count = 1

    compressed += s[-1] + str(count)
    return compressed


string = input("Enter a string: ")
print("Compressed String:", compress_string(string))
