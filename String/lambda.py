# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Syntax
# lambda arguments : expression

# x = lambda a, b, c, d: a ** 2 + b * 3 + c
# print(x(10, 2, 4, 89))

# Python Program to Find Numbers Divisible by Another Number using anonymous function
mylist = [13, 28, 54, 39, 102, 222, 89]
result =list(filter(lambda x: (x % 13 == 0), mylist))
print("Numbers d0ivisible by 13 are:", result)
