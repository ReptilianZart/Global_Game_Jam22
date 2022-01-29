import pygame

whiteCat = pygame.image.load("spriteFolder/whiteCat3.png")
CatSize = 64

blackCat = pygame.image.load("spriteFolder/blackCat.png")

background = pygame.image.load("spriteFolder/galaxy.png")

# MAIN MENU
pygame.font.init()

logo = pygame.image.load("spriteFolder/title.png")
title = pygame.image.load("spriteFolder/title.png")

arcadeFont1 = pygame.font.Font("fonts/arcade1.ttf", 22)
keyprompt1 = arcadeFont1.render("Press any key to continue", True, (255,255,255))
arcadeFont2 = pygame.font.Font("fonts/arcade1.ttf", 24)
keyprompt2 = arcadeFont2.render("Press any key to continue", True, (255,255,255))

creditFont = pygame.font.Font("fonts/arcade2.ttf", 15)
credit = creditFont.render("Created by ", True, (255,255,255))