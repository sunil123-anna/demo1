n= 18

guesscount=1
while(guesscount<=5):
    Enterednumber = int(input("enter your guess:"))
    if Enterednumber < n:
        print("Your guess is smaller !")
        print("Remaining guess:",5-guesscount)

    if Enterednumber > n:
        print("Your guess is greater!")
        print("Remaining guess:", 5-guesscount)

    if Enterednumber == n:
        print("Your guess is correct!")
        print("No. of guesses remaining:",5-guesscount)
        break
    guesscount=guesscount+1
print("Game over!")












