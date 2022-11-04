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
