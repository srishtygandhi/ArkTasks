# ~~~~~~~~~~ general instructions ~~~~~~~~~~~~~~~
#  1. to move the box left tilt ur face to left
#  2. to              right                right
#  3. to stop the box bring your face in middle of the camera
#  4. the line on the bottom is to tell u whether ur face is in left or middle or right

#importing libraries
import cv2
import numpy as np


cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

#ball
#initial position
ball_x = 50
ball_y = 50
#initial velocity
ball_vel_x = 2
ball_vel_y = 2

# initial position of block
# actual position of block
box_x = 320
# last recoreded position of face to increase somoothness in game
last_x = 320

#initial velocity of box
box_vel_x = 5

# initial score 
score = 0


#recognize when to change the velocity of box and ball
change_vel = False

#things needed to print text on screen
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
thickness = 2

# infinite game loop 
# to stop press q
while True :
    # reads from camera
    ret,frame = cap.read()
    

    # if nothing is read
    if ret == False:
        continue 
    # transform into gray image for cascade filter to work
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # detects face 
    faces = face_cascade.detectMultiScale(gray_frame, 1.5, 4) #1.5 scale up factor # number of nearest neighbour


    #border check
    if(ball_x > 590):
        ball_vel_x *= -1
    # left
    if(ball_x < 50):
        ball_vel_x *= -1
    # top
    if(ball_y < 50):
        ball_vel_y *= -1
    # bottom
    if (ball_y > 330 ):
        if (ball_x > box_x - 50 and ball_x < box_x + 50 ):
            ball_vel_y *= -1
            score += 1
            if score > 2:
                change_vel = True 
    # below bottom
    if(ball_y > 335):
        break

    #updates the position of ball
    ball_x += ball_vel_x
    ball_y += ball_vel_y

    

    

    # detecting co-ordinates of face 
    for(x, y, w, h) in faces:
        # mirror image rectify
        # window size 640*480
        pseudo_x = x + (w//2) - 320
        x_cord = 320 - pseudo_x 
        last_x = x_cord

    # background white colour
    cv2.rectangle(frame, (0,0),(640,480), (255,255,255), -1)
    
    # drawing guidelines and updating the position of the box
    if last_x >= 340 :  #mid = 320  +20
        if box_x <= 590:
            box_x += box_vel_x
        cv2.line(frame, (427,480), (640,480), (0,0,0), 15)
        cv2.line(frame, (427,480), (640,480), (0,255,0), 12)
        cv2.line(frame, (427,480), (640,480), (0,0,0), 3) # bottom right
        
    
    elif last_x <= 300:
        if box_x >= 50:
            box_x -= box_vel_x 
        cv2.line(frame, (0,480), (213,480), (0,0,0), 15)
        cv2.line(frame, (0,480), (213,480), (0,255,0), 12)
        cv2.line(frame, (0,480), (213,480), (0,0,0), 3) # bottom left line

    else:
        box_x = box_x
        cv2.line(frame, (213,480), (427,480), (0,0,0), 15)
        cv2.line(frame, (213,480), (427,480), (0,255,0), 12)
        cv2.line(frame, (213,480), (427,480), (0,0,0), 3) # bottom middle
    


    #draws circle for ball
    cv2.circle(frame, (ball_x, ball_y), 50, (0,0,255),-1)

    # drawing rctangle of face
    cv2.rectangle(frame, (box_x-50,380), (box_x + 50,480), (255,0,0), -1)

    


# increase level of game
# updating velocities
    if(change_vel): 
        if ball_vel_x > 0:
            ball_vel_x = score
        else:
            ball_vel_x = score*(-1)
        if ball_vel_y > 0:
            ball_vel_y = score
        else:
            ball_vel_y = score*(-1)
        
        if (score >5):
            box_vel_x = ((score//5) + 1 )*5 # change at multiple of 5
        # ball_vel_y += 1
        change_vel = False

    

    #printing necessary text on screen
    cv2.putText(frame, 'Score: ' + str(score),(00, 22), font, fontScale, (0,0,0), thickness, cv2.LINE_AA, False)
    cv2.putText(frame, 'Press Q to exit',(00, 50), font, fontScale, (0,0,0), thickness, cv2.LINE_AA, False)

    cv2.imshow("video",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


    

cap.release()
cv2.destroyAllWindows()