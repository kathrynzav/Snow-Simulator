import os
import random
import pygame
import math
import sys

screen = pygame.display.set_mode((510,510))
pygame.display.set_caption("snow storm simulator 1999")

running = 1
boxWidth = 25
boxHeight = 25
appleWidth = 10
appleHeight = 10

file = 'Christmas Bells-Sound Effect.wav'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(10)

class Player(object):
    def __init__(self):
        self.rect = pygame.rect.Rect((54,54,boxWidth,boxHeight))
    def keyInputs(self):
        key = pygame.key.get_pressed()
        dist = 1
        if key[pygame.K_LEFT]:
           self.rect.move_ip(-1, 0)
        if key[pygame.K_RIGHT]:
           self.rect.move_ip(1, 0)
        if key[pygame.K_UP]:
           self.rect.move_ip(0, -1)
        if key[pygame.K_DOWN]:
           self.rect.move_ip(0, 2)
        if self.rect.top > 511:
            self.rect.top = 0
        if self.rect.left > 511:
            self.rect.left = 0
    def draw(self, surface):
        pygame.draw.rect(screen,(255,255,255), self.rect)

randomX = 0
randomY = 0


class Apple(object):
    def __init__(self):
        self.rect = pygame.rect.Rect((randomX,randomY,boxWidth,boxHeight))
    def move(self):
        self.rect.top = randomY
        self.rect.right = randomX
    def draw(self, surface):
        pygame.draw.rect(screen, (255,255,255), self.rect)

player = Player()
apple  = Apple()
while running:
    done = False
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    screen.fill((65,105,255)) ##setting the bg color
    randomX = random.randint(1,510)
    randomY = random.randint(1,510)
    apple.draw(screen)
    player.draw(screen)
    player.keyInputs()
    apple.move()
    pygame.display.update()
    pygame.display.flip() ##refresh the screen
