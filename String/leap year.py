# A leap year is exactly divisible by 4 except for century years (years ending with 00).
# The century year is a leap year only if it is perfectly divisible by 400.

Year = int(input("enter year:"))
if(Year % 4 == 0):
    if(Year % 100 == 0):
        if(Year % 400 == 0):
            print(Year,"is a leap year!")
else:
    print(Year, "is not a leap Year")
