
        ### here we have imported random from library

import random
a = random.randint(50,100) ### random.randint will allow to choose a random number b/w 50 and 100
guess = int(input("Guess a number. "))
b = 1
while not guess == a:
    if guess > 100:
        print('The number entered is too high.') ### if the guess is high we will guess the number again
        guess = int(input("Guess a number. "))
    elif guess < 50:
        print('The number entered is too low.') ### if the guess is low we will guess the number again
        guess = int(input("Guess a number. "))
    elif not guess == a:
        guess = int(input("Guess a number. "))
    b += 1            ### this shows the number of tries a user has made to make a guess
print(f'Congratulation the number is guessed in {b} tries.')