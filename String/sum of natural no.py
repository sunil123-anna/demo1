num = int(input("Enter number:"))
sum = 0
if num < 0:
    print("Enter positive number!")

else:
    for i in range (1, num+1):
        sum = sum + i
    print("the sum of natural no.", num,":", sum)
