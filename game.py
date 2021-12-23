#############################
# Dino game                 #
# Version: Alpha -1.0       #
# Made by: Ladányi Attila   #
# Ha ellopod, buzi vagy xd  #
#############################

import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((800, 500))

icon = pygame.image.load('trex.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Dino game by Ladányi Attila")

# Trex

global playerY_change

playerImg = pygame.image.load('trex.png')
kaktuszImg = pygame.image.load('kaktusz.png')
playerX = 100
playerY = 250
playerY_change = 0
pont = False
pontok = 0

kaktuszX = 772

clock = pygame.time.Clock()


def player(x, y):
    screen.blit(playerImg, (x, y))


def kaktusz(x, y):
    screen.blit(kaktuszImg, (x, y))


font = pygame.font.SysFont('Times New Roman', 32)
szoveg = f"Pontok: {pontok}"
text = font.render(szoveg, False, (0, 0, 0))
halal = False

frames = 70
noveles = False

running = True
while running:

    screen.fill((255, 255, 255))

    screen.blit(text, (0, 0))

    if playerY <= 100:
        playerY = 100

    if playerY >= 250:
        playerY = 250

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerY_change = -5
            if event.key == pygame.K_DOWN or playerY == 95:
                playerY_change = 5
                pygame.event.clear()

        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_UP or event.key == pygame.K_DOWN):
                playerX_change = 0
                if playerY <= 100:
                    pass

    if playerY <= 100:
        playerY = 100
        playerY_change = 5

    if playerY >= 250:
        playerY = 250

    playerY += playerY_change

    player(playerX, playerY)

    if kaktuszX < 0:
        kaktuszX = 772

    if kaktuszX == 102:
        update()

    kaktusz(kaktuszX, 268)

    kaktuszX -= 5

    # Szöveg

    def update():
        global pontok
        global szoveg
        global text
        pontok += 1
        pont = False
        szoveg = f"Pontok: {pontok}"
        text = font.render(szoveg, False, (0, 0, 0))
        screen.blit(text, (0, 0))

    if kaktuszX == 102 and playerY + 20 > 268:
        death()

    def death():
        global running
        global halal
        meghal = font.render("Meghaltál!", False, (0, 0, 0))
        screen.blit(meghal, (400, 0))
        halal = True

    pygame.draw.line(screen, (0, 0, 0), (0, 315), (800, 315), width=1)

    pygame.display.update()

    if pontok % 10 == 0 and pontok != 0:
        noveles = True
        pontok += 1

    if noveles:
        noveles = False
        frames += 10

    clock.tick(frames)

    if halal:
        pygame.time.wait(2000)
        running = False
