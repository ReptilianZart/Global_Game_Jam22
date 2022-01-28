import pygame

import game
import global_variables as gv


"""
CHARACTER CLASS:

will handle movement, logic, health etc. of the character and its opposite


"""

startingX = 100
startingY = 100


# TEMPORARY SPRITES, will get from sprite.py later
whiteCat = pygame.image.load("spriteFolder\whiteCat")



class Character:
    def __init__(self):
        self.x = startingX
        self.y = startingY
        self.dx = 0
        self.dy = 0
    
    def draw(self):
        pass
