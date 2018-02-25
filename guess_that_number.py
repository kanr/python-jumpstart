# Guess that number
# Creates a random number and will loop prompting user for guess until number is correctly guessed.

import random
print('_______________________________')
print('Guess that number')
print('_______________________________')
print()

the_number = random.randint(0,100)
guess = -1

name = input('Player Name')

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number:
        #print('to low')
        print('Sorry {}, your guess of {} was to low'.format(name,guess))
    elif guess > the_number:
        #print('to high')
        print('Sorry {}, your guess of {} was to high'.format(name,guess))
    else:
        #print('you win')
        print('Winner! congrats {}, your guess of {} was correct'.format(name,guess))

print('done')
