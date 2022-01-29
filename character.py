import pygame

import global_variables as gv
import sprites as spr

"""
CHARACTER CLASS:

will handle movement, logic, health etc. of the character and its opposite

or will just hold the data of the player


"""

startingX = 100
startingY = 100

# Black Cat Position
wx = startingX
wy = startingY

# White Cat Position (opposite side of the screen)
bx = gv.SCREEN_WIDTH - startingX - 64
by = gv.SCREEN_HEIGHT - startingY - 64

def updatePos(self, change_x, change_y):
    self.wx += change_x
    self.wy += change_y

    self.bx -= change_x
    self.by -= change_y

    # adding boundary
    if self.wx < 0:
        self.wx = 0
    if self.wx > gv.SCREEN_WIDTH - spr.CatSize:
        self.wx = gv.SCREEN_WIDTH - spr.CatSize
    if self.wy < 0:
        self.wy = 0
    if self.wy > gv.SCREEN_HEIGHT - spr.CatSize:
        self.wy = gv.SCREEN_HEIGHT - spr.CatSize

    if self.bx < 0:
        self.bx = 0
    if self.bx > gv.SCREEN_WIDTH - spr.CatSize:
        self.bx = gv.SCREEN_WIDTH - spr.CatSize
    if self.by < 0:
        self.by = 0
    if self.by > gv.SCREEN_HEIGHT - spr.CatSize:
        self.by = gv.SCREEN_HEIGHT - spr.CatSize


# Change in position
dx = 0
dy = 0

# Momentum
mx = 0
my = 0

# Keep track of current directional keys being pressed
left = 0
right = 0
up = 0
down = 0


def movePlayer(self):
    self.dx = 0
    self.dy = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gv.EXITGAME = True
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.left = 1
            elif event.key == pygame.K_RIGHT:
                self.right = 1
            elif event.key == pygame.K_UP:
                self.up = 1
            elif event.key == pygame.K_DOWN:
                self.down = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.left = 0
            elif event.key == pygame.K_RIGHT:
                self.right = 0
            elif event.key == pygame.K_UP:
                self.up = 0
            elif event.key == pygame.K_DOWN:
                self.down = 0
    # sum the changes in position
    if (self.left):
        if (self.mx > -1):
            self.mx -= 0.1
        self.dx -= 3
    if (self.right):
        if (self.mx < 1):
            self.mx += 0.1
        self.dx += 3
    if ((self.left == 0 and self.right == 0) or (self.left == 1 and self.right == 1)):
        if (self.mx > 0.1):
            self.mx -= 0.1
        elif (self.mx < -0.1):
            self.mx += 0.1
        else:
            self.mx = 0
            
    if (self.up):
        if (self.my > -1):
            self.my -= 0.1
        self.dy -= 3
    if (self.down):
        if (self.my < 1):
            self.my += 0.1
        self.dy += 3
    if ((self.up == 0 and self.down == 0) or (self.up == 1 and self.down == 1)):
        if (self.my > 0.1):
            self.my -= 0.1
        elif (self.my < -0.1):
            self.my += 0.1
        else:
            self.my = 0


    # add momentum
    self.dx += self.mx
    self.dy += self.my


    updatePos(self, self.dx, self.dy)
                
    
