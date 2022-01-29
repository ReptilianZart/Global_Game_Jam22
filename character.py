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
    wx += change_x
    wy += change_y

    bx -= change_x
    by -= change_y
    
