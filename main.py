import pygame
from game import Game
import projectile
import sprites as spr
import global_variables as gv

g = Game()
g.init()




#############################################

"""
DEBUGGING

centre lines, shows centre lines of screen to see if stuff is positioned correctly

"""

class debug:
    def __init__(self):
        self.GREEN = (102, 255, 51)
        pass

    def guide_lines(self):
        # horizontal
        pygame.draw.line(g.screen, self.GREEN, (0, gv.SCREEN_HEIGHT/2), (gv.SCREEN_WIDTH, gv.SCREEN_HEIGHT/2))
        # vertical
        pygame.draw.line(g.screen, self.GREEN, (gv.SCREEN_WIDTH/2, 0), (gv.SCREEN_WIDTH/2, gv.SCREEN_HEIGHT))

    def draw_fps(self):
        fps = spr.creditFont.render(str(round(g.clock.get_fps())), True, (254,254,254))
        g.screen.blit(fps, (5,5))





#############################################


debug = debug()

while not gv.EXITGAME:
    
    g.run()
    g.update()
    #debug.guide_lines()
    #print(len(gv.projectiles))
    debug.draw_fps()

    pygame.display.flip()



