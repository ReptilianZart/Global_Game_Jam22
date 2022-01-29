import global_variables as gv
import projectile 
import sprites as spr
import character as player

import pygame

# Probs not gonna be used tbh, just use x,y seperately
class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y




"""
GAME CLASS:

Init the screen

might be going to hard on the oop lol


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

        """for event in pygame.event.get():    #outputs list of all current events
            if event.type == pygame.QUIT:
                gv.EXITGAME = True
                pygame.quit()"""



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
                self.game_state = "play"

        
    
    
    # Runs the game
    def playing(self):
        self.draw(spr.background, 0, 0)
        player.movePlayer(player)
        self.drawPlayer()

        # bullets
        self.test_bullets()

        self.check_Exit()
        

    def test_bullets(self):
        if self.counter > 50:
            self.counter = 0
            projectile.spawn_bullet(0,gv.SCREEN_HEIGHT/2)
        if self.counter == 25:
            projectile.spawn_bullet_list(gv.center_x, gv.center_y, projectile.bullet_circle)
        projectile.update_projectile()
        self.draw_bullets()

        self.counter += 1

    # Runs the game over screen
    def game_over(self):
        pass

    def draw(self, sprite, x, y):
        self.screen.blit(sprite, (x, y))

    def drawPlayer(self):
        self.draw(spr.blackCat, player.bx, player.by)
        self.draw(spr.whiteCat, player.wx, player.wy)

    def draw_bullets(self):
        for bullet in gv.projectiles:
            self.draw(spr.bullet, bullet.x, bullet.y)
            #pygame.draw.circle(self.screen, (255,255,255), (bullet.x, bullet.y))
            pass


    def check_Exit(self):
        for event in pygame.event.get():    #outputs list of all current events
            if event.type == pygame.QUIT:
                gv.EXITGAME = True
                pygame.quit()
    
    # loop which will run 
    def update(self):
        if (gv.EXITGAME):
            #return to prevent screen update error after quitting
            return
        self.clock.tick(self.fps)
        pygame.display.update()


