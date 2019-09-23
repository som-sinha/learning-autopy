# This program says hello and asks for my name
print('Hello World')

myName = input('What is your name? ')        # Ask for name and store it
print('It is good to meet you, ' + myName)
print('The length of your name is: ' + str(len(myName)))

myAge = input('What is you age? ')       # Ask for their age and store it
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
