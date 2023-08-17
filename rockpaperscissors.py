import random

human_score = 0
comp_score = 0

def game():

    actions = ('rock', 'paper', 'scissors')
    comp = random.choice(actions)
    global human_score 
    global comp_score
    human = input('Enter Rock, Paper, or Scissors: ')
    if human == 'quit': quit()
    human = human.lower()

    if human == comp:
        print("\nIt's a tie!")

    elif human == 'rock' and comp == 'paper':
        print('\nPaper covers rock! You Lose!')
        if comp_score == 0:
            comp_score = 1
        else:
            comp_score = comp_score + 1

    elif human == 'rock' and comp == 'scissors':
        print('\nRock smashes scissors! You win!')
        if human_score == 0:
            human_score = 1
        else:
            human_score = human_score + 1

    elif human == 'paper' and comp == 'rock':
        print('\nPaper covers rock! You Win!')
        if human_score == 0:
            human_score = 1
        else:
            human_score = human_score + 1

    elif human == 'paper' and comp == 'scissors':
        print('\nScissors cuts paper! You Lose!')
        if comp_score == 0:
            comp_score = 1
        else:
            comp_score = comp_score + 1

    elif human == 'scissors' and comp == 'paper':
        print('\nScissors cuts paper! You Win!')
        if human_score == 0:
            human_score = 1
        else:
            human_score = human_score + 1
        

    elif human == 'scissors' and comp == 'rock':
        print('\nRock smashes scissors! You Lose!')
        if comp_score == 0:
            comp_score = 1
        else:
            comp_score = comp_score + 1

    else:
        print('Enter a valid response')

while True:
    if human_score <5 and comp_score <5:
        game()
        print('Current Score: \n Human:',human_score, '\n Computer:',comp_score,'\n')
    else:
        if human_score == 5:
            print('You won the game!')
        else:
            print('Computer wins!')
        print('Final Score: \n Human:', human_score , '\n Computer:', comp_score,'\n')
        quit()