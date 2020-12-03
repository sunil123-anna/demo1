lower = 300
upper = 1000
# sum = 0

for num in range (lower, upper+1):
    # order = len(str(num))
    sum = 0

    temp = num
    while (temp > 0):
        digit = temp % 10
        sum = sum + digit ** 3
        temp = temp // 10
    if (sum == num):
        print(num)