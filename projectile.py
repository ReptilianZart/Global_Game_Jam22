from cmath import sqrt
from tkinter import CENTER
import pygame
import game as g
import global_variables as gv
import math

sqrt2 = round(math.sqrt(2), 1)/2

# directions
N = (0,-1)
NE = (sqrt2,-sqrt2)
E = (1,0)
SE = (sqrt2,sqrt2)
S = (0,1)
SW = (-sqrt2,sqrt2)
W = (-1,0)
NW = (-sqrt2,-sqrt2)

# some ready made sets of directions
bullet_circle = [N,NE,E,SE,S,SW,W,NW]





projectileX = 0
projectileY = 0

# one projectile object will be created for each bullet, then a list of bullets will be looped through using the fucntions below
class Projectile:
    def __init__(self, x, y, vector=(1,0)):
        #self.color = color
        #self.type = type
        self.x = x
        self.y = y
        self.vector = vector    # 2d vector to update x,y  using a vector instead of direction and speed cus it will go faster diagonally
        # can add if statements for type, which can decide which sprite to use and which speed to use



def spawn_bullet(x,y, vector = (1,0)):
    bullet = Projectile(x,y, vector)
    gv.projectiles.append(bullet)


def spawn_bullet_list(x,y, dir):
    for direc in dir:
        spawn_bullet(x, y, direc)


# function to run through the projectile list and update
def update_projectile():
    for proj in gv.projectiles:
        proj.x += proj.vector[0]
        proj.y += proj.vector[1]
        if proj.x > gv.SCREEN_WIDTH or proj.x < 0:
            gv.projectiles.remove(proj)
        elif proj.y > gv.SCREEN_HEIGHT or proj.y < 0:
            gv.projectiles.remove(proj)



# not used, instead its in game.py cus the g.screen is fucky
# function to run through the projectile list and update
def draw_projectile():
    for proj in gv.projectiles:
        pygame.draw.circle(g.screen, (255,255,255), (proj.x, proj.y))

    

