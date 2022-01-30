from numpy import character
import global_variables as gv
import projectile 
import sprites as spr
import character

import pygame
import math


# Probs not gonna be used tbh, just use x,y seperately
class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y




"""
GAME CLASS:

Init the screen



"""
class Game:
    def __init__(self):
        
        # The clock for setting the fps
        self.clock = pygame.time.Clock()
        self.fps = gv.FPS
        self.game_state = "menu"
        self.counter = 0



    def init(self):
        # Initialise pygame
        pygame.init()
        # Create the screen
        self.screen = pygame.display.set_mode((gv.SCREEN_WIDTH,gv.SCREEN_HEIGHT))

        #   Title and Icon (32x32)
        pygame.display.set_caption("DUALITY")



    def run(self):
        if self.game_state == "play":
            self.playing()
        elif self.game_state == "game_over":
            self.game_over()
        else:
            self.main_menu()





    """
    MAIN MENU STATE

    """

    # Runs the main menu
    def main_menu(self):

        # background
        self.draw(spr.background, 0, 0)
        self.draw(spr.logo, gv.SCREEN_WIDTH/2 - 230, gv.SCREEN_HEIGHT/2 - 250)
        self.draw(spr.title, gv.SCREEN_WIDTH/2 - 200, gv.SCREEN_HEIGHT/2 - 0)
        # press any key to continue
        if self.counter < 30:
            self.draw(spr.keyprompt1, gv.SCREEN_WIDTH/2 - 230, gv.SCREEN_HEIGHT/2 + 180)
        else:
            self.draw(spr.keyprompt2, gv.SCREEN_WIDTH/2 - 220, gv.SCREEN_HEIGHT/2 + 190)

        if self.counter > 60:
            self.counter = 0
        self.counter += 1


        # check to go to play
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gv.EXITGAME = True
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                self.start_game()

        


    """
    PLAY STATE
    
    """

    def start_game(self):
        self.game_state = "play"
        gv.projectiles = []
        self.player = character.Player()

    
    # Runs the game
    def playing(self):
        self.draw(spr.background, 0, 0)
        self.player.movePlayer()
        self.drawPlayer()

        # bullets
        self.test_bullets()

        # collision
        collision = self.check_collision()
        if collision:
            self.game_state = "menu"


    def test_bullets(self):
        if self.counter > 50:
            self.counter = 0
            projectile.spawn_bullet(0,gv.SCREEN_HEIGHT/2)
        if self.counter == 25:
            projectile.spawn_bullet_list(gv.center_x, gv.center_y, projectile.bullet_circle)
        projectile.update_projectile()
        self.draw_bullets()

        self.counter += 1


    def check_collision(self):
        for bullet in gv.projectiles:
            dist = get_distance(self.player.wx, self.player.wy, bullet.x, bullet.y)
            if dist < 32:
                return True
        return False


    def drawPlayer(self):
        self.draw(spr.blackCat, self.player.bx, self.player.by)
        self.draw(spr.whiteCat, self.player.wx, self.player.wy)

    def draw_bullets(self):
        for bullet in gv.projectiles:
            self.draw(spr.bullet, bullet.x, bullet.y)
            #pygame.draw.circle(self.screen, (255,255,255), (bullet.x, bullet.y))
            pass
    



    """
    GAME OVER STATE
    
    """

    # Runs the game over screen
    def game_over(self):
        game_over_background = pygame.image.load("game_over_background.jpg")
        self.screen.blit(game_over_background,0,0)
    

    """
    OTHER METHODS

    """

    
    def draw(self, sprite, x, y):
        self.screen.blit(sprite, (x, y))

    
    # loop which will run 
    def update(self):
        if (gv.EXITGAME):
            #return to prevent screen update error after quitting
            return
        self.clock.tick(self.fps)
        pygame.display.update()




"""
GENERIC FUNCTIONS

"""

def get_distance(x1, y1, x2, y2):
    return math.sqrt(pow(x1-x2,2) + pow(y1-y2,2))