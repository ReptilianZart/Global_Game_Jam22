import global_variables as gv
import projectile
import sprites

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
        self.game_state = "play"


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

        for event in pygame.event.get():    #outputs list of all current events
            if event.type == pygame.QUIT:
                gv.EXITGAME = True



    # Runs the main menu
    def main_menu(self):
        # background
        pass
    
    # Runs the game
    def playing(self):
        pass

    # Runs the game over screen
    def game_over(self):
        pass

    def draw(self, sprite, x, y):
        self.screen.blit(sprite, (x, y))

    
    # loop which will run while game_state == "playing"
    def update(self):
        self.clock.tick(self.fps)
        pygame.display.update()


