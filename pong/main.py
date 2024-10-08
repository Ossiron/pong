import pygame
import time
import random

pygame.init()

window  = pygame.display.set_mode([1280,720])
title = pygame.display.set_caption("pong")
win = pygame.image.load("pong/assets/win.png")

score1=0
score1_img = pygame.image.load("pong/assets/score/0.png")
score2=0
score2_img = pygame.image.load("pong/assets/score/0.png")


field = pygame.image.load("pong/assets/field.png")

player1 = pygame.image.load("pong/assets/player1.png")
player1_y = 300

player1_y_moveup=False
player1_y_movedown=False
player2_y_moveup = False
player2_y_movedown=False


player2 = pygame.image.load("pong/assets/player2.png")
player2_y = 300
#                           about the ball
ball = pygame.image.load("pong/assets/ball.png")
ball_x = 617
ball_y = 337
ball_dir = -5
ball_dir_y = 3
#                           funtions
def draw():
    if score1 < 9 and score2 < 9:
        window.blit(field,(0,0))
        window.blit(player1,(50,player1_y))
        window.blit(player2,(1150,player2_y))
        window.blit(ball,(ball_x,ball_y))
        window.blit(score1_img,(500,50))
        window.blit(score2_img,(710,50))  
        move_ball()
        move_player1()
        move_player2()
    else:
        window.blit(win,(300,330))


def move_player1():
    global player1_y
    
    if player1_y_moveup:
        player1_y -= 5
    else:
        player1_y += 0

    if player1_y_movedown:
        player1_y += 5
    else:
        player1_y += 0

    if player1_y <=0:
        player1_y =0
    elif player1_y >= 575:
        player1_y = 575
    #player1_y = ball_y - 46

def move_player2():
    global player2_y
    if player2_y_moveup:
            player2_y -= 5
    else:
            player2_y += 0

    if player2_y_movedown:
            player2_y += 5
    else:
            player2_y += 0

    if player2_y <=0:
            player2_y =0
    elif player2_y >= 575:
            player2_y = 575
    #player2_y = ball_y - 46

def move_ball():
    global ball_x
    global ball_y
    global ball_dir
    global ball_dir_y
    global score1
    global score2
    global score1_img
    global score2_img


    ball_x += ball_dir
    ball_y += ball_dir_y
    if ball_x < 120 and ball_x >110:
        if player1_y < ball_y +23:
            if player1_y + 146 > ball_y:
                ball_dir *= -1
                inverter = random.randint(0,1)
                if inverter == 0:
                    ball_dir_y*= -1

    if ball_x > 1100 and ball_x< 1110:
       if player2_y < ball_y +23:
            if player2_y + 146 > ball_y:
                ball_dir *= -1
                inverter = random.randint(0,1)
                if inverter == 0:
                    ball_dir_y*= -1
    if ball_y >= 700:
        ball_dir_y*= - 1
    elif ball_y <= 0:
        ball_dir_y*= -1
    if ball_x < -50:
        ball_x = 617
        ball_y = 337
        ball_dir_y*= -1
        ball_dir *= -1
        score2+= 1
        score2_img = pygame.image.load("pong/assets/score/" + str(score2)+".png")

    elif ball_x > 1320:
        ball_x = 617
        ball_y = 337
        ball_dir_y*= -1
        ball_dir *= -1
        score1+= 1
        score1_img = pygame.image.load("pong/assets/score/"+ str(score1)+".png")


loop = True

while loop:

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_w:
                player1_y_moveup = True
            if events.key == pygame.K_s:
                player1_y_movedown = True
            if events.key == pygame.K_UP:
                player2_y_moveup = True
            if events.key == pygame.K_DOWN:
                player2_y_movedown = True
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_w:
                player1_y_moveup = False
            if events.key == pygame.K_s:
                player1_y_movedown = False
            if events.key == pygame.K_UP:
                player2_y_moveup = False
            if events.key == pygame.K_DOWN:
                player2_y_movedown = False
            
            
        
    draw()
  
    pygame.display.update()