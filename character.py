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

def movePlayer(self):
    dx = 0
    dy = 0
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                gv.left = 1
            elif event.key == pygame.K_RIGHT:
                gv.right = 1
            elif event.key == pygame.K_UP:
                gv.up = 1
            elif event.key == pygame.K_DOWN:
                gv.down = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                gv.left = 0
            elif event.key == pygame.K_RIGHT:
                gv.right = 0
            elif event.key == pygame.K_UP:
                gv.up = 0
            elif event.key == pygame.K_DOWN:
                gv.down = 0
    # sum the changes in position
    if (gv.left):
        dx -= 3
    if (gv.right):
        dx += 3
    if (gv.up):
        dy -= 3
    if (gv.down):
        dy += 3
    updatePos(self, dx, dy)
                
    
