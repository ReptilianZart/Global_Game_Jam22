import pygame
from game import Game
import projectile
import sprites as spr
import global_variables as gv




g = Game()
g.init()


while not gv.EXITGAME:
    g.draw(spr.background, 0, 0)
    g.draw(spr.whiteCat, 800, 400)
    g.draw(spr.blackCat, 200, 200)
    g.run()
    g.update()
