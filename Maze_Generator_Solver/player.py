import pygame

class player:
    x = 10
    y = 10
    speed = 1

    def moveRight(self):
        self.x += self.speed
    def moveUp(self):
        self.y -= self.speed
    def moveLeft(self):
        self.x -= self.speed
    def moveDown(self):
        self.y += self.speed
