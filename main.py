import pygame
from game import Game
import projectile
import sprites as spr
import global_variables as gv




g = Game()
g.init()


while not gv.EXITGAME:
    g.draw(spr.whiteCat, 400, 400)
    g.run()
    g.update()
