def fun(a,b):
    add = a + b
    print(f"The Addition of a and b is {add}")

    sub = a - b
    print(f"The Substraction of a and b is {sub}")

    mul = a * b
    print(f"The Multiplication of a and b is {mul}")

    div = a / b
    print(f"The Division of a and b is {div}")

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
fun(a,b)
