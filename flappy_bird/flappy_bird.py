import cv2
import numpy as np
import random

bird_frame=1
bird_x = 200
bird_y = 200
bird_size=[40,30]
bird_image=[1,1]
bird_image[0]=cv2.imread(r'Flappy-Bird1.png')
bird_image[1]=cv2.imread(r'Flappy-Bird2.png')
bird_image[0] = cv2.resize(bird_image[0],(bird_size[0],bird_size[1]))
bird_image[1] = cv2.resize(bird_image[1],(bird_size[0],bird_size[1]))

pipes=[[350,200,False],[700,300,False],[1050,100,False]]#[pipe_position(convert) , gap_width ,pass or not]
pipe_width=70
pipe_gap = 150

speed = 15
score = 0
run = True

def draw_pipe(img):
    global score
    height = img.shape[0]
    for pipe in pipes:
        # draw upper pipes
        # draw lowwer pipes
        # move pipes
        if(pipe[0]<0):
            pipe[0] = max(pipes[0][0],pipes[1][0],pipes[2][0])+350
            pipe[1] = random.randint(100,300) 
            pipe[2] = False
        if pipe[0]+pipe_width<bird_x and pipe[2]==False:
            # rules : add score
            pipe[2]=True

def draw_bird(img):
    global run, bird_frame
    # detact face
    for(x,y,w,h)in faceRect:
        # cv2.rectangle(frame,(?,?),(?,?),(0,255,0),2)
        cv2.rectangle(frame,(0,255,0),2) # mark the face
        # set y cordinate of bird  
    img[bird_y:bird_y+bird_size[1],bird_x:bird_x+bird_size[0]]=bird_image[bird_frame]
    if bird_frame==0:
        bird_frame=1
    else:
        bird_frame=0
    for pipe in pipes:
        # when will game over
        if ():
            run=False
            break
def game_over(img):
    # draw last score player get
    cv2.putText(img,"press q to quit the game",(50,200),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
    return 0

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame,(0,0),fx=1.2,fy=1.2)
        gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        if(run==True):
            draw_pipe(frame)
            draw_bird(frame)
            # draw current score
        else:
            game_over(frame)
        cv2.imshow('flappy bird',frame)
    else:
        break
    if cv2.waitKey(10)==ord('q'):
        break