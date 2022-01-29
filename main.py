import pygame
from game import Game
import projectile
import sprites as spr
import global_variables as gv


g = Game()
g.init()


while not gv.EXITGAME:
    g.draw(spr.background, 0, 0)
    #g.draw(spr.blackCat, c.getX(), c.getY())
    g.drawPlayer()
    g.run()
    g.update()
