n1 = int(input("Enter your first number: "))
n2 = int(input("Enter your second number: "))
z = input("Enter your operation ")

if z == "+":
    if n1 == 56 and n2 == 9:
        print("answer is 45.")
    else:
        print("Answer is ", n1 + n2)
elif z == "-":
    print("Answer is ", n1 - n2)
elif z == "*":
    if n1 == 45 and n2 == 3:
        print("Answer is 44.")
    else:
        print("answer ", n1 * n2)
elif z == "/":
    if n1 == 56 and n2 == 6:
        print(" answer 100")
    else:
        print("answer is ", n1 / n2)