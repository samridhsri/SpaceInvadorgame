# Space-invasion-game
import random

import pygame
import math

pygame.init()


# defined functions
def score(x, y):
    score = fontuse.render("Score: " + str(valscore), True, (255, 255, 255))
    screen.blit(score, (x, y))


def gameovertext():
    gameover = fontuse.render("Game Over", True, (255, 255, 255))
    myname = fontuse.render("By Samridh", True, (255, 255, 255))
    surname = fontuse.render("Srivastava", True, (255, 255, 255))
    screen.blit(gameover, (420, 350))
    screen.blit(myname, (420, 350))
    screen.blit(surname, (420, 350))


def jet():
    screen.blit(jetimg, (jetx, jety))


def fire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))


def monster(x, y, i):
    screen.blit(allmonsterimg[i], (x, y))


def isCollision(monsterx, monstery, bulletx, bullety):
    distance = math.sqrt(math.pow(monsterx - bulletx, 2) + (math.pow(monstery - bullety, 2)))
    if distance < 27:
        return True
    else:
        return False


# font
scorefont = pygame.font.Font('ZenTokyoZoo-Regular.ttf', 30)
fontuse = pygame.font.Font('ZenTokyoZoo-Regular.ttf', 44)
# Screen is of 400x600
screen = pygame.display.set_mode((1000, 650))

# score

valscore = 0

textx = 5
texty = 5

# jet image and position
jetimg = pygame.image.load('jet-fighter.png')
jetx = 165
jety = 550
jet_change = 0

# bullet
bulletimg = pygame.image.load('bullet.png')
bullety = 595
bulletx = 0
bullety_change = -1
bullet_state = "ready"

# monster

allmonsterimg = []
monsterx = []
monstery = []
monsterx_change = []
monstery_change = []
num_of_monsters = 6

for i in range(num_of_monsters):
    allmonsterimg.append(pygame.image.load('monster.png'))
    monsterx.append(random.randint(0, 1000))
    monstery.append(random.randint(0, 150))
    monsterx_change = 1
    monstery_change = 0.9

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
                jet_change = -1
            if event.key == pygame.K_RIGHT:
                print("Right Key is pressed")
                jet_change = 1
            if event.key == pygame.K_SPACE:
                print("Space is pressed")
                bulletx = jetx
                fire(bulletx, bullety)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                jet_change = 0

    # Monster movement
    for i in range(num_of_monsters):
        if monstery[i] > 500:
            for j in range(num_of_monsters):
                monstery[j] = 2000
            gameovertext()
            break

        monsterx[i] = monsterx[i] + monsterx_change
        if monsterx[i] <= 0:
            monsterx_change = 0.3
            monstery[i] = monstery[i] + monstery_change
        elif monsterx[i] > 900:
            monsterx_change = -0.3
            monstery[i] = monstery[i] + monstery_change

        collision = isCollision(monsterx[i], monstery[i], bulletx, bullety)
        if collision:
            bullety = 480
            bullet_state = "ready"
            valscore = valscore + 1
            monsterx[i] = random.randint(0, 355)
            monstery[i] = random.randint(30, 150)

        monster(monsterx[i], monstery[i], i)

    # Jet Movement

    jetx = jetx + jet_change
    if jetx <= 0:
        jetx = 0
    elif jetx >= 900:
        jetx = 900

    # bullet movement
    if bullety <= 0:
        bullety = 508
        bullet_state = "Ready"
    if bullet_state == "fire":
        fire(bulletx, bullety)
        bullety = bullety + bullety_change
    jet()
    score(textx, texty)

    pygame.display.update()
