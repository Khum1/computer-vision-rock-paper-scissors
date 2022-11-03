# Computer Vision Rock, Paper, Scissors

In this project I have created a game of Rock, Paper, Scissors using python and machine learning. The purpose of this project was to build on my knowledge of python and OOP, and start expanding my knowledge into machine learning and using cv2 to operate and get data from the camera.

**Technologies used:**

- Python
- [Teachable Machine](https://teachablemachine.withgoogle.com/) - This has allowed me to make a model which will predict the poses the user makes. 
- Tensorflow - Used in conjunction with Teachable Machine to process the model.
- OpenCV-Python - used to process the image from the camera 

## Milestone 1

Using Teachable Machine I created the keras_model.h5 for the Rock, Paper, Scissors game, training the model with images from my webcam of the Rock, Paper and Scissors poses as well as doing nothing. After training, this model predicts what pose the user is holding up to the camera or if they are not holding up a pose.


## Milestone 2

I created the game Rock, Paper, Scissors. The game will ask the user for their decision - 'Rock, Paper or Scissors...?' as an input. It will then compare this with a randomly selected choice from the computer using the get_winner() function to decide who won the game. If you win it prints "You won!", if you lose it prints "You lose!" and if both answers are the same it prints "You tied."



``` python
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



def get_winner(computer_choice, user_choice):
    if user_choice == computer_choice:
        print('You tied.')
    elif user_choice == 'Rock' and computer_choice == 'Scissors' or user_choice == 'Paper' and computer_choice == 'Rock' or user_choice == 'Scissors' and computer_choice == 'Paper':
        print('You won!')
    else:
        print('You lose!')

def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    print(f'The computer chose {computer_choice}')
    get_winner(computer_choice, user_choice)

play()
```
![] (Screenshots/RPS1.PNG)

## Milestone 3

