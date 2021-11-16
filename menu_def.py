from classes.Dino import Dino
from classes.Cloud import Cloud
from classes.Obstacles import LargeCactus, SmallCactus, Bird
from pygame.locals import *
import random
import os
from global_parameters import Parameters
import pygame
# from start_run_def import startRun

# pygame.init()

def menu(ifdead):
    # run = True
    Parameters.isRunnung = True
    print("Parameters.isRunnungedwf", Parameters.isRunnung)
    Parameters.screen = pygame.display.set_mode((Parameters.WIDTH, Parameters.HEIGHT))
    # while run:
    while Parameters.isRunnung:
        Parameters.screen.fill(Parameters.WHITE)

        font = pygame.font.Font("freesansbold.ttf", 30)

        if ifdead is False:
            text = font.render("Press any Key to Start", True, (0, 0, 0))

        elif ifdead is True:
            text = font.render("Press any Key to Restart", True, (0, 0, 0))
            score = font.render("Your Score: " + str(Parameters.point), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (Parameters.WIDTH // 2, Parameters.HEIGHT // 2 + 50)
            Parameters.screen.blit(score, scoreRect)

        textRect = text.get_rect()
        textRect.center = (Parameters.WIDTH//2, Parameters.HEIGHT // 2)
        Parameters.screen.blit(text, textRect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # run = False
                Parameters.isRunnung = False

                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                # startRun()
                Parameters.isRunnung = True

return Parameters.isRunnung