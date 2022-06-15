import random

def guess(x):
    random_number = random.randint(1,20)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and 20: '))
        if guess < random_number:
            print('Sorry to low, try again!')
        elif guess > random_number:
            print('Sorry to high, try again!') 
    print(f'Yay!! You guessed the right number!! Great Job!') 

guess(10)              