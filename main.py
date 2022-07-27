# start of first game using pycharm
#  space invaders ( from YouTube )

import pygame

# initialize pygame
pygame.init()
#  create screen display
screen = pygame.display.set_mode((800, 600))
screen.fill('white')
running = True  # value assigned to check if window running
#  Title and focus
pygame.display.set_caption('Space Invaders')
pygame.display.set_icon(pygame.image.load('ufo.png'))
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
def player():
    screen.blit(playerImg,(playerX,playerY))

# Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player()
    pygame.display.update() # updates the window
