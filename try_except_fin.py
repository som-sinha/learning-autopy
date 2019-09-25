try:
    print('Gimme a number: ', end='')
    num = int(input())
    print(num)
except ValueError:
    print('Please input a valid value')
    print('You screwed it up now run the program again...')
finally:
    print('Fin.')
