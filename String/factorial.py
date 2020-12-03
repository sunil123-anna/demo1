# 4! = 4*3*2*1
num = int(input("Enter number:"))
factorial = 1
if (num < 0):
    print("Factorial number doesn't exist for negative values!")
elif (num == 0):
    print("Factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("Factorial of", num, "is:", factorial)
