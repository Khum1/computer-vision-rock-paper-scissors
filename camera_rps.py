import RPS_Template
import random
import numpy as np
import cv2
RPS_Template

class RPS:
    def __init__(self):
        self.options = ['Rock', 'Paper', 'Scissors', 'Nothing']
        self.user_wins = 0
        self.computer_wins = 0



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


    def get_prediction(self):
        prediction = RPS_Template.prediction[0]
        print(prediction)
        max_index = np.argmax(prediction)
        user_choice = self.options[max_index]
        print(max_index)
        return user_choice


def play():
    game = RPS()
    print('Start')
    while game.user_wins <3 or game.computer_wins <3:
        computer_choice = game.get_computer_choice()
        user_choice = game.get_prediction()
        print(f'The computer chose {computer_choice}')
        print(f'You chose {user_choice}')
        game.get_winner(computer_choice, user_choice)
        if game.user_wins == 3:
            print('Congrats you won!')
            break
        elif game.computer_wins == 3: 
            print("You lose!")
            break
        print('Stop')
    print('Start2')
    RPS_Template.cap.release()
    cv2.destroyAllWindows()
    


play()