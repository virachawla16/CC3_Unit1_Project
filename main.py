import random
number = random.randint(1, 10)
guesses = 0

q1 = input('How are you?')

print('Good to know!')

name = input('What is your name?')

print('Hello' + name + 'I am guessing a number between 1-10')

while guesses != number:

    if guesses < number:
        print('Oops! You guessed too low')
    if guesses > number:
        print('Oops! You guessed too high')
    if guesses == number:
        print('Good job! You guessed correctly!')


