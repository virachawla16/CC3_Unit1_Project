import random

n = random.randint(1, 10)
guesses = 0   # this is because the player hasn't yet made a guess
count = 1    # this is used to tell the player how many times it took them to guess the correct number


introduction = ('Hello', 'Hi there!', 'Welcome', 'Hey')
greeting = random.choice(introduction)
print(greeting)

name = raw_input(greeting + ', What is your name?' + ":")

print(greeting + name + 'Welcome to Guess A Random Number.')
print('In this game, I will generate a random number between 1-10 and you have to guess what number I chose. Enjoy!!')
print('I am now choosing a number between 1-10.')

while guesses != n:
    guesses = input('Go on, guess a number between 1-10!' ":")

if guesses.isdigit():
    guesses = int(guesses)

    if guesses == n:
        print('Good job! You guessed correctly!')
    elif guesses < n:
        print('Oops! You guessed too low. Try again!')
        count += 1  # if the user guesses wrong, we add one to the count. it shows that they get another guess.
    else:
        print('Oops! You guessed too high. Try again!')
        count += 1

        print('It took you', count, 'tries! Not bad :)')