import cv2

def countdown(t):
    while t > 0:
        min, sec = divmod(t,60)
        timer = f'{min}, {sec}'
        print(sec, end='\r')
        cv2.waitKey(1000)
        t -= 1


countdown(3)