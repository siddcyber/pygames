# start of first game using pycharm
#  space invaders ( from youtube )

import pygame
# initialize pygame
pygame.init()
#  create screen display
screen = pygame.display.set_mode((800,600))
running = True # value assigned to check if window running
#  Title and focus
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('ufo.png')

# Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
