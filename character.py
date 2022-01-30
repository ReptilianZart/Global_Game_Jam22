import pygame

import global_variables as gv
import sprites as spr

"""
CHARACTER CLASS:

will handle movement, logic, health etc. of the character and its opposite

or will just hold the data of the player


"""
class Player:
    def __init__(self):
        self.startingX = 100
        self.startingY = 100

        # Black Cat Position
        self.wx = self.startingX
        self.wy = self.startingY



        # White Cat Position (opposite side of the screen)
        self.bx = gv.SCREEN_WIDTH - self.startingX - 64
        self.by = gv.SCREEN_HEIGHT - self.startingY - 64


        # update center of cat
        # center coordinates for collision
        self.centre_wx = self.wx + 32
        self.centre_wy = self.wy + 32
        self.centre_bx = self.bx + 32
        self.centre_by = self.by + 32


        # Change in position
        self.dx = 0
        self.dy = 0

        # Momentum
        self.mx = 0
        self.my = 0

        # Keep track of current directional keys being pressed
        self.left = 0
        self.right = 0
        self.up = 0
        self.down = 0


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




    def movePlayer(self):
        self.dx = 0
        self.dy = 0
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                gv.EXITGAME = True
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.left = 1
                    print("LEFT_P")
                if event.key == pygame.K_RIGHT:
                    self.right = 1
                    print("RIGHT_P")
                if event.key == pygame.K_UP:
                    self.up = 1
                    print("UP_P")
                if event.key == pygame.K_DOWN:
                    self.down = 1
                    print("DOWN_P")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.left = 0
                    print("LEFT_R")
                if event.key == pygame.K_RIGHT:
                    self.right = 0
                    print("RIGHT_R")
                if event.key == pygame.K_UP:
                    self.up = 0
                    print("UP_R")
                if event.key == pygame.K_DOWN:
                    self.down = 0
                    print("DOWN_R")
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


        self.updatePos(self.dx, self.dy)
                
    
