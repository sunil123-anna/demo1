terms = int(input("How many terms?"))
n1, n2 = 0, 1
count = 0
if (terms == 1):
    print("Fibonacci Sequence upto:", terms)
    print(n1)
elif (terms <= 0):
    print("Enter a positive number!")
else:
    print("Fibonacci Sequence:")
    while (count < terms):
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
