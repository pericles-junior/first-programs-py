import os

msgWel = 'Welcome to the game "Guess the Secret Number" 🤔'
print('-' * len(msgWel))
print(msgWel)
print('-' * len(msgWel))
secret = 9
attempts = 0

while True:
  try:
    shot = int(input('Type the shoot between 1 a 10: '))
    attempts += 1
    if shot == secret and attempts == 1:
      print(f'Congratulations!! You tried {attempts} once. 👏👏👏')
      break
    elif shot == secret and attempts > 1:
      print(f'Congratulations!! You tried {attempts} times. 👏👏👏')
      break
    else:
      print('Wrong! Try again!')
  except ValueError:
    print('Invalid attempt! Type just numbers!')