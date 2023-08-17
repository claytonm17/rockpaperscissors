import random
actions = ('Rock', 'Paper', 'Scissors')
comp = random.choice(actions)
print(comp)
action = input('Enter Rock, Paper, or Scissors: ')
if action == comp:
    print("It's a tie!")

elif action == 'Rock' and comp == 'Paper':
    print('You Lose!')
elif action == 'Rock' and comp == 'Scissors':
    print('You win!')

elif action == 'Paper' and comp == 'Rock':
    print('You Win!')
elif action == 'Paper' and comp == 'Scissors':
    print('You Lose!')

elif action == 'Scissors' and comp == 'Paper':
    print('You Win!')
elif action == 'Scissors' and comp == 'Rock':
    print('You Lose!')

else:
    print('Enter a valid response')
