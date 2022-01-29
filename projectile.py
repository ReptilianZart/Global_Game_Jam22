import pygame
import game as g
import global_variables as gv


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



def spawn_bullet(x,y):
    bullet = Projectile(x,y)
    gv.projectiles.append(bullet)


# function to run through the projectile list and update
def update_projectile():
    for proj in gv.projectiles:
        proj.x += proj.vector[0]
        proj.y += proj.vector[1]



# function to run through the projectile list and update
def draw_projectile():
    for proj in gv.projectiles:
        pygame.draw.circle(g.screen, (255,255,255), (proj.x, proj.y))

    

