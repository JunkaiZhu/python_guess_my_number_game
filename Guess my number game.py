high = 100
low = 0
print("Please think of a number between 0 and 100!")
guessed = False
while not guessed:
    guess = (high + low)//2
    print("Is your secret number" + str(guess) + "?")
    y = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if y == 'h':
        high = guess
    elif y == 'l':
        low = guess
    elif y == 'c':
        guessed = True
        print("Game over. Your secret number was: " + str(guess))
    else:
        print("Sorry, I did not understand your input.")
        
