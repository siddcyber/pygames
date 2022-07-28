# start of first game using pycharm
#  space invaders ( from YouTube )

import pygame
import random

# initialize pygame
pygame.init()
#  create screen display
xAxis = 800
yAxis = 600
screen = pygame.display.set_mode((xAxis, yAxis))
running = True  # value assigned to check if window running
#  Title and focus
pygame.display.set_caption('Space Invaders')
pygame.display.set_icon(pygame.image.load('ufo.png'))

#  player section
playerImg = pygame.image.load("player.png")
playerX = xAxis * 0.46
playerY = yAxis * 0.8
playerXChange = 0
playerYChange = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# Enemy section
enemyImg = pygame.image.load("enemy.png")
enemyX = random.randint(0, int(xAxis - 64))
enemyY = random.randint(0, int(yAxis * 0.65))
enemyXChange = 4
enemyYChange = 40


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Game Loop
while running:
    screen.fill('black')  # the screen fil is set here to update the screen black after every event
    screen.blit(pygame.image.load("background.png"), (0, 0)) # adding bg image (slows loop)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # to check if key was pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXChange = -5
            if event.key == pygame.K_RIGHT:
                playerXChange = 5
            if event.key == pygame.K_UP:
                playerYChange = -5
            if event.key == pygame.K_DOWN:
                playerYChange = 5

        # to check if key was released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXChange = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerYChange = 0
    # adding changes to player x and y to show in the defined function as a new value
    playerX += playerXChange
    playerY += playerYChange
    # setting boundary by if function to delete and reset when near some value
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:  # keep in mind the pixels of te image
        playerX = 736
    if playerY <= 0:
        playerY = 0
    elif playerY >= 536:
        playerY = 536
    #  enemy settings
    enemyX += enemyXChange
    if enemyX <= 0:
        enemyXChange = 4
        enemyY += enemyYChange
    elif enemyX >= 736:  # keep in mind the pixels of the image
        enemyXChange = -4
        enemyY += enemyYChange

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()  # updates the window
