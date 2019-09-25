# Containes a bit of every concept learned up until https://youtu.be/48WXHT0dfEY?list=PLGoJzB271_7r-iLYuEHEPJ5pSIYxXjJEn

from random import randint

while True:
    # Choosing upper limit
    UPPER_LIMIT = randint(10, 100)

    # Creating a random secret number
    secretNum = randint(0, UPPER_LIMIT)

    # Asking user to guess number
    print('I am thinking of a number between 0 and ', str(UPPER_LIMIT))
    win = False

    # Guessing Game
    for i in range(1, 11):
        print('Can you guess it? ', end = '')
        try:
            guess = int(input())
        except ValueError:
            print('Please enter a correct value. (For example 1 instead of 1.0 or one)')
        if guess == secretNum:
            print('Hell Yeah! The number is ' + str(secretNum))
            if i == 1:
                print('You got it on you first try!!! \n You\'re on FIREEE!')
            else:
                print('It took you ' + str(i) + ' tries to guess it.')
            win = True
            break
        elif guess > secretNum:
            print('Guess Lower')
        elif guess < secretNum:
            print('Guess Higher')
        if i == 9:
            print('Okay now last guess, i\'ll give a better clue')
            print('Think "closer"  to ' + str(secretNum + 1))
    if not win:
        print('Well tried.')
        print('The number was ' + str(secretNum))

    print('Wanna try again? (y for yes; n for no)')
    play = input()
    if play != 'y':
        break
