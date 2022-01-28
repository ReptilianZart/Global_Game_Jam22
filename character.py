import pygame

import game
import global_variables as gv


"""
CHARACTER CLASS:

will handle movement, logic, health etc. of the character and its opposite


"""

startingX = 100
startingY = 100

sens = 150


# TEMPORARY SPRITES, will get from sprite.py later
#whiteCat = pygame.image.load("spriteFolder\whiteCat")



class Character:
    def __init__(self):
        self.x = startingX
        self.y = startingY
        self.dx = 0
        self.dy = 0
    
    # gets keyboard inputs and updates position of character
    def update_pos(self):
        for event in pygame.event.get():    #outputs list of all current events
            # move, not diagonally yet
            if event.type == pygame.KEYUP:
                self.dy = sens
            elif event.type == pygame.KEYDOWN:
                self.dy = sens
            elif event.type == pygame.K_RIGHT:
                self.dx = sens
            elif event.type == pygame.K_LEFT:
                self.dx = -sens

            # resets the change, when keystroke is released
            if event.type == pygame.KEYUP:
                self.dx = 0
                self.dy = 0

        self.x += self.dx
        self.y += self.dy

        print("update_pos")

