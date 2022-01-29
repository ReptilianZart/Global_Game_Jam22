from click import prompt
import pygame

pygame.font.init()

whiteCat = pygame.image.load("spriteFolder/whiteCat3.png")

blackCat = pygame.image.load("spriteFolder/blackCat.png")

background = pygame.image.load("spriteFolder/galaxy.png")


# MAIN MENU
logo = pygame.image.load("spriteFolder/title.png")
title = pygame.image.load("spriteFolder/title.png")

arcadeFont1 = pygame.font.Font("fonts/ka1.ttf", 22)
keyprompt1 = arcadeFont1.render("Press any key to continue", True, (255,255,255))
arcadeFont2 = pygame.font.Font("fonts/ka1.ttf", 24)
keyprompt2 = arcadeFont2.render("Press any key to continue", True, (255,255,255))

creditFont = pygame.font.Font("fonts/arcade2.ttf", 15)
credit = creditFont.render("Created by ", True, (255,255,255))