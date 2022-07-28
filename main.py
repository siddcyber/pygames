# start of first game using pycharm
#  space invaders ( from YouTube )

import pygame

# initialize pygame
pygame.init()
#  create screen display
length = 800
width = 600
screen = pygame.display.set_mode((length, width))
running = True  # value assigned to check if window running
#  Title and focus
pygame.display.set_caption('Space Invaders')
pygame.display.set_icon(pygame.image.load('ufo.png'))
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerXChange = 0
playerYChange = 0


def player(x, y):
    screen.blit(playerImg, (x, y))

# Game Loop
while running:
    screen.fill('black')  # the screen fil is set here to update the screen black after every event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # to check if key was pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXChange = -1
            if event.key == pygame.K_RIGHT:
                playerXChange = 1
            if event.key == pygame.K_UP:
                playerYChange = -1
            if event.key == pygame.K_DOWN:
                playerYChange = 1

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
    elif playerX>= 736:  # keep in mind the pixels of te image
        playerX = 736
    if playerY <=0:
        playerY = 0
    elif playerY>=536:
        playerY=536
    player(playerX, playerY)
    pygame.display.update()  # updates the window

