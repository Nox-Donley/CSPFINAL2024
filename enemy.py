#enemy.py
import pygame
import random
import math

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

class enemy:
    def __init__(self):
        self.xpos = 400
        self.ypos = 200
        self.direction = RIGHT
        self.isAlive = True

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 255), (self.xpos, self.ypos, 30, 30))

    def move(self,map, ticker, px, py):
        if ticker%40 == 0:
            num = random.randrange(0,4)
            if num == 0:
                self.direction = RIGHT
            elif num == 1:
                self.direction = LEFT
            elif num == 2:
                self.direction = UP
            elif num == 3:
                self.direction = DOWN
        if abs(int(py/50)-int(self.ypos/50))<2:
            if px < self.xpos:
                self.xpos-=5
                self.direction = LEFT
            else:
                self.xpos+=5
                self.direction = RIGHT
        if abs(int(px/50)-int(self.xpos/50))<2:
            if py < self.ypos:
                self.ypos-=5
                self.direction = UP
            else:
                self.ypos+=5
                self.direction = DOWN
        if self.direction == RIGHT and map[int((self.ypos)/50)][int( (self.xpos +20)/50)] == 2:
            self.direction = UP
            self.xpos -= 6
        if self.direction == LEFT and map[int((self.ypos)/50)][int( (self.xpos -20)/50)] == 2:
            self.direction =  DOWN
            self.xpos +=6
        if self.direction == DOWN and map[int((self.ypos)/50)][int( (self.xpos +20)/50)] == 2:
            self.direction = LEFT
            self.ypos -= 6
        if self.direction == UP and map[int((self.ypos)/50)][int( (self.xpos -20)/50)] == 2:
            self.direction =  RIGHT
            self.xpos +=6
        if self.direction == RIGHT:
            self.xpos +=3
        elif self.direction == LEFT:
            self.xpos -=3
        elif self.direction == UP:
            self.xpos -=3
        elif self.direction == DOWN:
            self.xpos +=3
    def die(self, ballx, bally):
        if math.sqrt((self.xpos-ballx)**2 +(self.ypos-bally)**2) <=20:
            self.isAlive = False