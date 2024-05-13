import pygame
import math

#CONSTANTS
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SPACE = 4
W = 5


class player:
    def __init__(self):
        #player variables
        self.xpos = 400 #xpos of player
        self.ypos = 415 #ypos of player
        self.vx = 0 #x velocity of player
        self.vy = 0 #y velocity of player
        self.direction = RIGHT
        self.health = 200

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 255), (self.xpos, self.ypos, 30, 30))
    
    def move(self, keys, map, direction):
        #LEFT MOVEMENT
        if keys[LEFT] == True:
            self.vx = -3
            self.direction = LEFT
            print("moving left")
        #RIGHT MOVEMENT
        elif keys[RIGHT] == True:
            self.vx = 3
            self.direction = RIGHT
        elif keys[UP] == True:
            self.vy = -3
            self.direction = UP
        elif keys[DOWN] == True:
            self.vy = 3
            self.direction = DOWN
        #turn off x velocity
        else:
            self.vx = 0
            self.vy = 0
            

        #COLLISION
        #left collision
        if map[int((self.ypos + 5) / 50) ][int((self.xpos - 10) / 50)] == 2 :
            self.xpos += 3
        #right collision
        if map[int((self.ypos) / 50) ][int((self.xpos +30 + 5) / 50)] == 2:
            self.xpos -= 3
        if map[int((self.ypos - 10) / 50) ][int((self.xpos) / 50)] == 2:
            self.ypos += 3
        if map[int((self.ypos+30) / 50) ][int((self.xpos+30 +5) / 50)] == 2:
            self.ypos -= 3
        self.xpos+=self.vx
        self.ypos += self.vy #update player xpos
        
    def hurt(self, enemyx, enemyy):
        if math.sqrt((self.xpos-enemyx)**2 +(self.ypos-enemyy)**2) <=20:
            self.health -= 2