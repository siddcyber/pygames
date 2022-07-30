# start of first game using pycharm
#  space invaders ( from YouTube )
# bug: when reaching the bulletX axis the score increases regardless of the player position
# bug: position of bullet fixed and updates score when in ready state
# bug:if playerY axis is different the bulletY axis does not follow
# bug: the game over loop do not remove the images to 2000 pixel position
import pygame
import math
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

# background sound
pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)

#  player section
playerImg = pygame.image.load("player.png")
playerX = xAxis * 0.46
playerY = yAxis * 0.8
playerXChange = 0
playerYChange = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# Enemy section
enemyImg = []
enemyX = []
enemyY = []
enemyXchange = []
enemyYchange = []
enemyNum = 10
for i in range(enemyNum):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0, int(xAxis - 64)))
    enemyY.append(random.randint(0, int(yAxis * 0.65)))
    enemyXchange.append(4)
    enemyYchange.append(40)


def enemy(x, y, num):
    screen.blit(enemyImg[num], (x, y))


# Bullet section
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = yAxis * 0.8
bulletXChange = 4
bulletYChange = 10
bulletState = "ready"
score = 0
textX = xAxis * 0.01
textY = yAxis * 0.01


def showScore(x, y):
    scoreFontRender = pygame.font.SysFont('arial', 32).render("score :" + str(score), True, "white")
    screen.blit(scoreFontRender, (x, y))

def showGameover():
    gameOverRender = pygame.font.SysFont('arial', 64).render("gameOver", True, "white")
    screen.blit(gameOverRender, (xAxis*0.35, yAxis*0.5))
def bullet(x, y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


#  collision detection section
def collision(enemyXaxis, enemyYaxis, bulletXaxis, bulletYaxis):
    distance = math.sqrt(math.pow(enemyXaxis - bulletXaxis, 2) + math.pow(enemyYaxis - bulletYaxis, 2))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
while running:
    screen.fill('black')  # the screen fil is set here to update the screen black after every event
    screen.blit(pygame.image.load("background.png"), (0, 0))  # adding bg image (slows loop)
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
            if event.key == pygame.K_SPACE:
                if bulletState == "ready":
                    # bullet sound
                    pygame.mixer.Sound('laser.wav').play()
                    bulletX = playerX

                    bullet(playerX, bulletY)

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
    for i in range(enemyNum):
        if enemyY[i] > 0:
            for j in range(enemyNum):
                # enemyY[i] = 2000
                enemyY[j] = 2000
                showGameover()
                break

        if enemyX[i] <= 0:
            enemyXchange[i] = 4
            enemyY[i] += enemyYchange[i]
        elif enemyX[i] >= 736:  # keep in mind the pixels of the image
            enemyXchange[i] = -4
            enemyY[i] += enemyYchange[i]
        isCollision = collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if isCollision:
            # enemy collision sound
            pygame.mixer.Sound('explosion.wav').play()

            bulletY = yAxis * 0.8
            bulletState = "ready"
            score += 1
            print(score)
            enemyX[i] = random.randint(0, int(xAxis - 64))
            enemyY[i] = random.randint(0, int(yAxis * 0.65))
        enemy(enemyX[i], enemyY[i], i)
        enemyX[i] += enemyXchange[i]

    #     bullet movement
    if bulletState == "fire":
        bullet(bulletX, bulletY)
        bulletY -= bulletYChange
    if bulletY <= 0:
        bulletY = yAxis * 0.8
        bulletState = "ready"

    player(playerX, playerY)
    showScore(textX, textY)
    pygame.display.update()  # updates the window
