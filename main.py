# start of first game using pycharm
#  space invaders ( from YouTube )

import pygame

# initialize pygame
pygame.init()
#  create screen display
screen = pygame.display.set_mode((800, 600))
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
                playerXChange = -0.1
            if event.key == pygame.K_RIGHT:
                playerXChange = 0.1
            if event.key == pygame.K_UP:
                playerYChange = -0.1
            if event.key == pygame.K_DOWN:
                playerYChange = 0.1

        # to check if key was released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXChange = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerYChange = 0
    playerX += playerXChange
    playerY += playerYChange
    player(playerX, playerY)
    pygame.display.update()  # updates the window
#
