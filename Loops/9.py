# Program to find prime or not

num = int(input("Enter the number: "))
flag = False

if num == 1:
    print("1 is the Natural number")

elif num>1:
    for i in range(2,num):
        if num%i == 0:
            flag = True

    if flag:
        print("not")
    else:
        print("prime")

else:
    print("Enter valid number")
