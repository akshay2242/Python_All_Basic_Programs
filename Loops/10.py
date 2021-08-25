# Program to check string is Palindrome or not

str = input("Enter the name ")

pal = str[::-1]

if str == pal:
    print("Given string is Palindrome")
else:
    print("Given string is not Palindrome")
