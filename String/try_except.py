print("Enter number1:")
a = input()
print("Enter number2:")
b = input()

try:
    print("The sum of two numbers is:", int(a) + int(b))
except Exception as e:
    print(e)

print("This is important line")


def function1(a, b):
    # a = 1
    # b = 20
    return (a + b)

s = function1(20, 30)
print(s)
