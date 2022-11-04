# Computer Vision Rock, Paper, Scissors

In this project I have created a game of Rock, Paper, Scissors using python and machine learning. The purpose of this project was to build on my knowledge of python and OOP, and start expanding my knowledge into machine learning and using cv2 to operate and get data from the camera.

**Technologies used:**

- Python
- [Teachable Machine](https://teachablemachine.withgoogle.com/) - This has allowed me to make a model which will predict the poses the user makes. 
- Tensorflow - Used in conjunction with Teachable Machine to process the model.
- OpenCV-Python - used to process the image from the camera 

## Milestone 1

Using Teachable Machine I created the keras_model.h5 for the Rock, Paper, Scissors game, training the model with images from my webcam of the Rock, Paper and Scissors poses as well as doing nothing. After training, this model predicts what pose the user is holding up to the camera or if they are not holding up a pose.
This was then checked by using RPS_Template to ensure 4 predictions are being output from the model - one for each probability that it is Rock, Paper, Scissors, or Nothing.


## Milestone 2

In this milestone I created the game Rock, Paper, Scissors using an input. The game will ask the user for their decision - 'Rock, Paper or Scissors...?' as an input. It will then compare this with a randomly selected choice from the computer using the get_winner() function to decide who won the game. If you win it prints "You won!", if you lose it prints "You lose!" and if both answers are the same it prints "You tied."



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

In this milestone I used the model created in Milestone 1 and the hame created in Milestone 2 to create a game of Rock, Paper Scissors which can be played against the computer using a camera input. To do this I created a class (RPS) which uses the get_computer_choice(), and get_winner() methods from my initial game and some methods split from the RPS_Template - display_camera(), predict_model() and end_game(). 

I then created the get_prediction() method, which takes the output of the model and gets the index of the most likely prediction of what is being shown to the camera. This is then compared against the choices in the options list in the __init__() method.

The play function combines the aspects of the game, repeating it until either the user or the computer has won 3 times.

To this I added a countdown to allow the user time to change their input.


``` python
import random
import numpy as np
import cv2
import time
from keras.models import load_model
from math import floor

class RPS:
    def __init__(self):
        self.options = ['Rock', 'Paper', 'Scissors', 'Nothing']
        self.user_wins = 0
        self.computer_wins = 0
        self.model = load_model('keras_model2.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        self.frame = []
        self.prediction = []

    def get_computer_choice(self):
        self.computer_choice = (random.choice(self.options[0:3]))

    def get_winner(self):
        if self.user_choice == self.computer_choice:
            print('You tied.')
        elif (self.user_choice == 'Rock' and self.computer_choice == 'Scissors') or\
             (self.user_choice == 'Paper' and self.computer_choice == 'Rock') or\
                 (self.user_choice == 'Scissors' and self.computer_choice == 'Paper'):
            print('You won!')
            self.user_wins += 1
        else:
            print('You lose!')
            self.computer_wins += 1

    def get_prediction(self):
        print(self.prediction)
        max_index = np.argmax(self.prediction)
        self.user_choice = self.options[max_index]

    def countdown(self, t, start_time):
        elapsed_time = time.time() - start_time
        min, sec = divmod(int(4 - elapsed_time),60)
        timer = f'{sec}'
        print(timer, end='\r')
        return t - elapsed_time > 0

    def display_camera(self):
        ret, self.frame = self.cap.read()     
        resized_frame = cv2.resize(self.frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        self.data[0] = normalized_image
        cv2.imshow('frame', self.frame)
        cv2.waitKey(1)

    def predict_model(self):
        self.prediction = self.model.predict(self.data)

    def end_game(self):
            self.cap.release()
            cv2.destroyAllWindows()
        
def play():
    game = RPS()
    start_time = time.time()
    while game.user_wins <3 or game.computer_wins <3: 
        start_time = time.time()       
        while game.countdown(3, start_time) == True:
            game.display_camera()
            
        game.predict_model()
        computer_choice = game.get_computer_choice()
        game.get_prediction()
        print(f'The computer chose {game.computer_choice}')
        print(f'You chose {game.user_choice}')
        game.get_winner()

        if game.user_wins == 3:
            print('Congrats you won the game!')
            game.end_game()
            break
        elif game.computer_wins == 3: 
            print("You lost the game!")
            game.end_game()
            break
        elif cv2.waitKey(1) & 0xFF == ord('q'):
            game.end_game()
            break

play()

```

[]!(Screenshots/RPS2.png)

## Conclusion

This task taught me basic computer vision skills, how to create and use a model from a different source and improved my python skills. 

To improve the game you could displaythe timer, or the prediction of the pose that you are currently showing, on the screen.