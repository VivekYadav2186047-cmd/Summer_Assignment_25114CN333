#Write a program to Count vowels and consonants.
string = input("enter the string =")
sum = 0
consonant = 0
vowels = ['a' , 'e ' , 'i' , 'o' ,'u']

for char in string:
    if(char in vowels):
        sum+=1
    else:
        consonant+=1
print("vowels =" , sum)
print("consonant" , consonant)
