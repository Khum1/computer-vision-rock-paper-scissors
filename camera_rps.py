import random
import numpy as np
import cv2
import time
from keras.models import load_model

class RPS:
    def __init__(self, frame, prediction):
        self.options = ['Rock', 'Paper', 'Scissors', 'Nothing']
        self.user_wins = 0
        self.computer_wins = 0
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        self.frame = frame
        self.prediction = prediction


    def get_computer_choice(self):
        computer_choice = (random.choice(self.options[0:3]))
        return computer_choice



    def get_winner(self,computer_choice, user_choice):
        if user_choice == computer_choice:
            print('You tied.')
        elif (user_choice == 'Rock' and computer_choice == 'Scissors') or\
             (user_choice == 'Paper' and computer_choice == 'Rock') or\
                 (user_choice == 'Scissors' and computer_choice == 'Paper'):
            print('You won!')
            self.user_wins += 1
        else:
            print('You lose!')
            self.computer_wins += 1


    def get_prediction(self, prediction):
        print(prediction)
        max_index = np.argmax(prediction)
        user_choice = self.options[max_index]
        print(max_index)
        return user_choice


    def countdown(self, t, start_time):
        elapsed_time = time.time() - start_time
        min, sec = divmod(elapsed_time,60)
        timer = f'{min}, {sec}'
        # print(timer, end='\r')
        if t - elapsed_time < 0:
            return False
        return True
            
    def display_camera(self, data, cap):
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        cv2.imshow('frame', frame)
        cv2.waitKey(1)

    def predict_model(self, model, data, frame):
        self.prediction = model.predict(data)
        

frame = []
prediction = []


def play():
    game = RPS(frame, prediction)
    start_time = time.time()
    while game.user_wins <3 or game.computer_wins <3: 
        start_time = time.time()       
        while game.countdown(5, start_time) == True:
            game.display_camera(game.data, game.cap)
            
        game.predict_model(game.model, game.data, game.frame)
        computer_choice = game.get_computer_choice()
        user_choice = game.get_prediction(game.prediction)
        print(f'The computer chose {computer_choice}')
        print(f'You chose {user_choice}')
        game.get_winner(computer_choice, user_choice)

        if game.user_wins == 3:
            print('Congrats you won the game!')
        elif game.computer_wins == 3: 
            print("You lost the game!")
        elif cv2.waitKey(1) & 0xFF == ord('q'):
            game.cap.release()
            cv2.destroyAllWindows()

play()