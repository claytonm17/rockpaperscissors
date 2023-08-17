import random
actions = ('rock', 'paper', 'scissors')
comp = random.choice(actions)
action = input('Enter Rock, Paper, or Scissors: ')
action = action.lower()

if action == comp:
    print("It's a tie!")

elif action == 'rock' and comp == 'paper':
    print('You Lose!')
elif action == 'rock' and comp == 'scissors':
    print('You win!')

elif action == 'paper' and comp == 'rock':
    print('You Win!')
elif action == 'paper' and comp == 'scissors':
    print('You Lose!')

elif action == 'scissors' and comp == 'paper':
    print('You Win!')
elif action == 'scissors' and comp == 'rock':
    print('You Lose!')

else:
    print('Enter a valid response')
