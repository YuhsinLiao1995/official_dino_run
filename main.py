import os
import random
import threading
import pygame

# Global constant
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100

pygame.init()

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BG = pygame.image.load(os.path.join("assets/Other", "Track.png")).convert()
bg_height = BG.get_height()

x_bg = 0
y_bg = SCREEN_HEIGHT - bg_height

def main():

#test2

    # BG = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
    run = True

    while run:
        SCREEN.blit(BG, (x_bg, y_bg))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
    pygame.quit()

main()
