import random

options = ['Rock', 'Paper', 'Scissors']
user_choice = ''
computer_choice = ''

def get_computer_choice(computer_choice):
    computer_choice = (random.choice(options))
    return computer_choice

def get_user_choice(user_choice):
    user_choice = input('Rock, Paper, Scissors...?')
    while True:
        if user_choice.capitalize() in options:
            return user_choice.capitalize()
        else:
            print('That is not an option.')
            user_choice = input('Rock, Paper, Scissors...?')

computer_choice = get_computer_choice(computer_choice)
user_choice = get_user_choice(user_choice)

print(computer_choice)
print (user_choice)


if user_choice == computer_choice:
    print('You tied.')
elif user_choice == 'Rock' and computer_choice == 'Scissors' or user_choice == 'Paper' and computer_choice == 'Rock' or user_choice == 'Scissors' and computer_choice == 'Paper':
    print('You won!')
else:
    print('You lose!')
