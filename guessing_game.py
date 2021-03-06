import random
import os
import sys

fruits = [
    'apple',
    'banana',
    'orange',
    'coconut',
    'strawberry',
    'lime',
    'grapefruit',
    'lemon',
    'kumquat',
    'blueberry',
    'melon'
]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def draw(bad_guesses, good_guesses, secret_word):
    clear()

    print('Strikes: {}/7'.format(len(bad_guesses)))
    print('')

    for letter in bad_guesses:
        print(letter, end=' ')
    print('\n\n')

    for letter in secret_word:
        if letter in good_guesses:
            print(letter, end='')
        else:
            print('_', end='')
    print('')


def get_guess(guesses):
    while True:
        guess = input("Guess a letter:  ").lower()

        if len(guess) != 1:
            print("you can only guess a single letter!")
        elif guess in guesses:
            print("You've already guessed that letter!")
        elif not guess.isalpha():
            print("You can only guess letters!")
        else:
            return guess


def play(done):
    clear()
    secret_word = random.choice(fruits)
    bad_guesses = set()
    good_guesses = set()
    word_set = set(secret_word)

    while True:
        draw(bad_guesses, good_guesses, secret_word)
        guess = get_guess(bad_guesses | good_guesses)

        if guess in word_set:
            good_guesses.add(guess)
            if not word_set.symmetric_difference(good_guesses):
                print('You win')
                print(f'The secret word was {secret_word}')
                done = True
        else:
            bad_guesses.add(guess)
            if len(bad_guesses) == 7:
                draw(bad_guesses, good_guesses, secret_word)
                print('You lost!')
                print(f'The secret word was {secret_word}')
                done = True
        if done:
            play_again = input('Play again? Y/n ').lower()
            if play_again != 'n':
                return play(done=False)
            else:
                print('Thank you for playing')
                sys.exit()


def welcome():
    start = input('Press enter/return to start or Q to quit ').lower()
    if start.lower() == 'q':
        print('Thank you for playing')
    else:
        return True

print('Welcome to Guessing Game')

done = False

while True:
    clear()
    welcome()
    play(done)