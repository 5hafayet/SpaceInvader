import pygame

# initializing the pygame
pygame.init()

# Title and Icon
pygame.display.set_caption("SpaceInvader")
icon = pygame.image.load('Icon/ufo.png')
pygame.display.set_icon(icon)

# create the screen
screen = pygame.display.set_mode((800, 600))

# Player
playerImg = pygame.image.load('Icon/player_ufo.png')
playerX = 370
playerY = 480
playerX_change = 0;


def player(x, y):
    screen.blit(playerImg, (playerX, playerY))


# Game loop
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0;
    playerX += playerX_change
    player(playerX, playerY)
    pygame.display.update()
