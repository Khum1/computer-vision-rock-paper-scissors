import random

options = ['Rock', 'Paper', 'Scissors']

def get_computer_choice():
    computer_choice = (random.choice(options))
    return computer_choice

def get_user_choice():
    user_choice = input('Rock, Paper, Scissors...?')
    while True:
        if user_choice.capitalize() in options:
            return user_choice.capitalize()
        else:
            print('That is not an option.')
            user_choice = input('Rock, Paper, Scissors...?')

computer_wins = 0
user_wins = 0

def get_winner(computer_choice, user_choice):
    if user_choice == computer_choice:
        print('You tied.')
    elif user_choice == 'Rock' and computer_choice == 'Scissors' or user_choice == 'Paper' and computer_choice == 'Rock' or user_choice == 'Scissors' and computer_choice == 'Paper':
        print('You won!')
        user_wins+=1
    else:
        print('You lose!')
        computer_wins+=1

def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    print(f'The computer chose {computer_choice}')
    get_winner(computer_choice, user_choice)

play()