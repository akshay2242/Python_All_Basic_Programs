# Program to print largest number among three numbers


a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

if a>b and a>c:
    print("a is largest number")

elif b>a and b>c:
    print("b is largest number")

else:
    print("c is largest number")
