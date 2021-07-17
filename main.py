# Space-invasion-game


import pygame
import math


#defined functions
def jet():
    screen.blit(jetimg, (jetx, jety))


def fire(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))

pygame.init()

#jet image and position
jetimg = pygame.image.load('jet-fighter.png')
jetx = 165
jety = 510
jet_change = 0

#bullet
bulletimg = pygame.image.load('bullet.png')
bullety = 508
bulletx = 0
bullety_change = -1
bullet_state = "ready"




screen = pygame.display.set_mode((400, 600))


# gameloop
running = True
while running:
    screen.fill((0, 0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left key is pressed")
                jet_change = -5
                jetx = jetx + jet_change
            if event.key == pygame.K_RIGHT:
                print("Right Key is pressed")
                jet_change = 5
                jetx = jetx + jet_change
            if event.key == pygame.K_SPACE:
                print("Space is pressed")
                bulletx = jetx
                fire(bulletx, bullety)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                jet_change = 0
    #Jet Movement
    


    #bullet movement
    if bullety<=0:
        bullety = 508
        bullet_state = "Ready"
    if bullet_state is "fire":
        fire(bulletx, bullety)
        bullety = bullety + bullety_change
    jet()

    pygame.display.update()
