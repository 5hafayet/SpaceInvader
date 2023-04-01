import pygame
import random

# initializing the pygame
pygame.init()

# Title and Icon
pygame.display.set_caption("SpaceInvader")
icon = pygame.image.load('Img/ufo.png')
pygame.display.set_icon(icon)

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("Img/background.png")

# Player
playerImg = pygame.image.load('Img/player_ufo.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('Img/enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.3
enemyY_change = 40


def player(x, y):
    screen.blit(playerImg, (playerX, playerY))


def enemy(x, y):
    screen.blit(enemyImg, (enemyX, enemyY))


# Game loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background,(0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # player position change based on key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    playerX += playerX_change

    # code to restrict player in the game frame
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736

    # enemy movement
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    if enemyX > 736:
        enemyX_change = -0.3
        enemyY += enemyY_change
    # Game over logic
    # if enemyY >= playerY-50:
    #     if enemyX > playerX-50 or enemyX < playerX + 50:
    #         print("Game Over")

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
