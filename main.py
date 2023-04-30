import math
import random

import pygame

# initializing the pygame
pygame.init()

# Title and Icon
pygame.display.set_caption("SpaceInvader")
icon = pygame.image.load('img/ufo.png')
pygame.display.set_icon(icon)

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("img/background.png")

score = 0

# Player
playerImg = pygame.image.load('img/player_ufo.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('img/enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.7
enemyY_change = 40

# Bullet
bulletImg = pygame.image.load('img/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
bullet_State = 'ready'      # ready = bullet not visible, fire = visible


def fire_bullet(x, y):
    global bullet_State
    bullet_State = 'fire'
    screen.blit(bulletImg, (x+16, y+10))


def player(x, y):
    screen.blit(playerImg, (playerX, playerY))


def enemy(x, y):
    screen.blit(enemyImg, (enemyX, enemyY))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX)**2 + (enemyY - bulletY)**2)
    if distance <= 27:
        return True
    else:
        return False

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # player position change based on key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.6
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.6
            if event.key == pygame.K_SPACE:
                if bullet_State == 'ready':
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
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

    # bullet movement
    if bulletY < 0:
        bulletY = 480
        bullet_State = 'ready'
    if bullet_State == 'fire':
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change
    if isCollision(enemyX, enemyY,bulletX,bulletY):
        bulletY = 480
        score+=1
        print(score)
        enemyX = random.randint(0, 800)
        enemyY = random.randint(50, 150)
        bullet_State='ready'


    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
