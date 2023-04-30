import math
import random

import pygame
from pygame import mixer

# initializing the pygame
pygame.init()

# Title and Icon
pygame.display.set_caption("SpaceInvader")
icon = pygame.image.load('img/ufo.png')
pygame.display.set_icon(icon)

# create the screen
screen = pygame.display.set_mode((801, 600))

# Background
background = pygame.image.load("img/background.png")

# Backgroud sound
mixer.music.load('sounds/background.wav')
mixer.music.play(-1)

# Score
score_value = 0
font = pygame.font.Font('fonts/Brief_River.ttf', 32)
textX = 10
textY = 10

# game over text
over_font = pygame.font.Font('fonts/Brief_River.ttf',64)
# Game over
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (0, 255, 0))
    screen.blit(over_text,(200,250))


def show_score(x, y):
    score = font.render("Score: "+str(score_value), True, (0, 255, 0))
    screen.blit(score, (x, y))


# Player
playerImg = pygame.image.load('img/player_ufo.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemies = 6

for i in range(no_of_enemies):
    enemyImg.append(pygame.image.load('img/enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyY_change.append(40)
    if(i%2):
        enemyX_change.append(-1.2)
    else:
        enemyX_change.append(1.3)

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


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


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
                bullet_sound = mixer.Sound('sounds/laser.wav')
                bullet_sound.play()
                if bullet_State == 'ready':
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
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
    for i in range(no_of_enemies):
        # Game over logic
        if enemyY[i] > 440:
            for j in range(no_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] > 736:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]


        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound('sounds/explosion.wav')
            explosion_sound.play()
            bulletY = 480
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
            bullet_State = 'ready'
        enemy(enemyX[i], enemyY[i], i)

    # bullet movement
    if bulletY < 0:
        bulletY = 480
        bullet_State = 'ready'
    if bullet_State == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX,textY)
    pygame.display.update()
