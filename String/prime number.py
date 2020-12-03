# num = int(input("Enter Number: "))
# if(num > 1):
#     for i in range(2, num):
#         if(num % i) == 0:
#             print(num, "is not prime number")
#             print(i,"times",num//i,"is equals to",num)
#             break
#     else:
#          print(num,"is a prime number")
# else:
#     print(num,"is not prime number")


# print prime numbers in an interval
lower = 100
upper = 300
print("All the prime numbers between",lower,"and", upper,"are:")
for num in range(lower, upper + 1):
    if (num > 1):
        for i in range(2, num):
            if(num % i == 0):
                print(num)
                break
        else:
            print(num)



