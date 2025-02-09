import cv2
import numpy as np
import random

bird_frame=1
bird_x = 200
bird_y = 200
bird_size=[40,30]
bird_image=[cv2.imread(r'Flappy-Bird1.png'),cv2.imread(r'Flappy-Bird2.png')]# if not work, change the path to absolute path
bird_image[0] = cv2.resize(bird_image[0],(bird_size[0],bird_size[1]))
bird_image[1] = cv2.resize(bird_image[1],(bird_size[0],bird_size[1]))

pipes=[[0,200,False],[-350,300,False],[-700,100,False]]#[pipe_position(convert) , gap_width ,pass or not]
pipe_width=70
pipe_gap = 150

speed = 15
score = 0
run = True

def draw_pipe(img):
    # your code (to draw the pipe and determine whether the bird pass the pipe)
    return 0

def draw_bird(img):
    # your code (to draw the bird and determine whether the bird overlaps with the pipe)
    return 0
def game_over(img):
    # your code (to draw the game over scene)
    return 0

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame,(0,0),fx=1.2,fy=1.2)
        if(run==True):
            # your code (to detect face and produce bird's position)
            draw_pipe(frame)
            draw_bird(frame)
            # your code (to draw score)
        else:
            game_over(frame)
        cv2.imshow('flappy bird',frame)
    else:
        break
    if cv2.waitKey(10)==ord('q'):#press q to quit the game
        break