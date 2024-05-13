import pygame
from player import player
from fireball import fireball
from enemy import enemy
pygame.init()
pygame.display.set_caption("top down grid game") # sets the window title
screen = pygame.display.set_mode((500, 500)) # creates game screen
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

p1 = player()
ball = fireball()
e1 = enemy()

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SPACE = 4
W = 5
keys = [False, False, False, False, False,]
ticker = 0



map = [[2,2,2,2,2,2,2,2,2,2],
       [2,0,0,0,0,2,2,0,0,2],
       [2,0,0,0,0,2,2,0,0,2],
       [2,0,0,2,2,2,2,0,0,2],
       [2,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,2],
       [2,0,2,0,0,0,2,2,0,2],
       [2,0,2,0,0,0,2,2,0,2],
       [2,0,2,0,0,0,0,0,0,2],
       [2,2,2,2,2,2,2,2,2,2]]

brick = pygame.image.load('brick.jpg')
dirt = pygame.image.load('dirt.png')

while not gameover:#GAME LOOP
    clock.tick(60) #FPS
    ticker += 1
    #input section-
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys [LEFT] = True
            elif event.key == pygame.K_RIGHT:
                keys [RIGHT] = True
            elif event.key == pygame.K_UP:
                keys [UP] = True
            elif event.key == pygame.K_DOWN:
                keys [DOWN] = True
            elif event.key == pygame.K_SPACE:
                keys [SPACE] = True

        if event.type == pygame. KEYUP:
                if event.key == pygame.K_LEFT:
                    keys[LEFT] = False
                elif event.key == pygame.K_RIGHT:
                    keys[RIGHT] = False
                elif event.key == pygame.K_UP:
                    keys[UP] = False
                elif event.key == pygame.K_DOWN:
                    keys[DOWN] = False
                elif event.key == pygame.K_SPACE:
                    keys [SPACE] = False
    #physics section-
    if p1.health >=1:
        p1.move(keys, map, RIGHT)
    if keys[SPACE] == True:
        ball.shoot(p1.xpos, p1.ypos, p1.direction)
    ball.move()
    if e1.isAlive == True:
        e1.move(map, ticker, p1.xpos, p1.ypos)
        p1.hurt(e1.xpos, e1.ypos)
    e1.die(ball.xpos, ball.ypos)
    #render section-
    
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
    #draw map
    for i in range(10):
        for j in range(10):
            if map[i][j] == 0:
                screen.blit(dirt, (j * 50, i * 50), (0, 0, 50, 50))
            if map[i][j] == 2:
                screen.blit(brick, (j * 50, i * 50), (0, 0, 50, 50))
    if p1.health >=1:        
        p1.draw(screen)
    if e1.isAlive == True:
        e1.draw(screen)
    if ball.isAlive == True:
        ball.draw(screen)
    pygame.draw.rect(screen, (255, 255, 255), (20, 465, 200, 30))
    pygame.draw.rect(screen, (150,0,0), (20, 465, p1.health, 30))
    pygame.draw.rect(screen, (0,0,0), (20,465,200,30), 3)

    pygame.display.flip()#this actually puts the pixel on the screen
    if p1.health <1:
        gameover = True

#end game loop=
pygame.quit()