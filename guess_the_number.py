import random
def guess_the_number(x):
  random_number = random.randint(1, x)
  guess=int(input(f'Guess a number between 1 and {x}: '))
  while guess != random_number:
    if guess < random_number:
      print('Sorry, guess again. Too low.')
    else:
      print('Sorry, guess again. Too high.')
    guess = int(input(f'Guess a number between 1 and {x}: '))
  print(f'Yay, congrats. You have guessed the number {random_number} correctly!')
guess_the_number(10)