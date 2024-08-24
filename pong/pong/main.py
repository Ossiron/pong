import pygame
import time


pygame.init()

window  = pygame.display.set_mode([1280,720])
title = pygame.display.set_caption("pong")

field = pygame.image.load("pong/assets/field.png")

player1 = pygame.image.load("pong/assets/player1.png")

player2 = pygame.image.load("pong/assets/player2.png")

ball = pygame.image.load("pong/assets/ball.png")
ball_x = 617
ball_y = 337
def draw():
    window.blit(field,(0,0))
    window.blit(player1,(50,300))
    window.blit(player2,(1150,300))
    window.blit(ball,(ball_x,ball_y))


def move_ball():
    global ball_x
    global ball_y

    ball_x+=1

loop = True

while loop:

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False
    draw()
    move_ball()
    pygame.display.update()