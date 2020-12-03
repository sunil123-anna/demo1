# Quadratic equation: ax**2 + bx + c
# solution is: -b +- under root b square minus 4 ac upon 2a
import cmath

a = int(input("Enter no1:"))
b = int(input("Enter no2:"))
c = int(input("Enter no3:"))

# calculate discrimination
d = (b ** 2) - (4 * a * c)

# two solutions
solu1 = (-b + cmath.sqrt(d)) / (2 * a)
solu2 = (-b - cmath.sqrt(d)) / (2 * a)

print("The solutions are {0} and {1}".format(solu1, solu2))
