# Program to find Armstrong number or not

num = int(input("Enter a three digit number: "))
sum = 0
temp = num

if (len(str(num)))==3:
    while num>0:
        m = num%10
        sum += (m**3)
        num = num//10

    if sum==temp:
        print("Given number is a Armstrong number")
    else:
        print("Given number is not a Armstrong number")   

else:
    print("Please enter valid number")

