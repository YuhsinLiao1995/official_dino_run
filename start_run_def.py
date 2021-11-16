from classes.Dino import Dino
from classes.Cloud import Cloud
from classes.Obstacles import LargeCactus, SmallCactus, Bird
from pygame.locals import *
import random
import os
from global_parameters import Parameters
import pygame
# from menu_def import menu


def startRun():
    global speedgame, obstacles
    # all variables
    Parameters.point = 0
    Parameters.ifdead = False
    player = Dino()
    cloud = Cloud(Parameters.WIDTH)

    pygame.display.set_icon(Parameters.logo)
    pygame.display.set_caption("Chrome Dino Runner")

    def score():
        global  speedgame
        Parameters.point += 1
        font = pygame.font.Font("game_over.ttf", 70)
        text = font.render("Point: " + str(Parameters.point), True, Parameters.FONT_COLOR)
        textRect = text.get_rect()
        textRect.center = (Parameters.WIDTH - 150, Parameters.HEIGHT // 3)
        Parameters.screen.blit(text, textRect)
        pygame.display.update()

    # displaying the background
    img_coordinates = (x_pos, y_pos) = (
        0, Parameters.HEIGHT - 5*Parameters.bg_height)  # coordinates of the background
    Parameters.screen.blit(Parameters.bg_img, (x_pos, y_pos))
    Parameters.screen.blit(Parameters.bg_img, (x_pos + Parameters.bg_width, y_pos))

    # making the game run
    run = True
    speedgame = 10  # speed at which the background will move
    pause = False

    # managing obstacles
    obstacles = []

    # managing pause and unpause
    def paused():
        pause = True
        font = pygame.font.Font("game_over.ttf", 90)
        text = font.render("Game Paused, Press 'u' to Unpause",
                           True, Parameters.FONT_COLOR)
        text_rect = text.get_rect()
        text_rect.center = (Parameters.WIDTH//2, Parameters.HEIGHT//3)
        Parameters.screen.blit(text, text_rect)
        pygame.display.flip()

        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_u:
                    pause = False
                    run = True

    def unpause():
        print("we want to unpause")
        pause = False
        run = True

    while run:

        # font = pygame.font.Font("freesansbold.ttf", 30)

        # we make the run possible to quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                run = False
                paused()

        # we make the background loop
        # we color the rest of the background in white
        Parameters.screen.fill(Parameters.WHITE)
        # we make the image appear one time
        Parameters.screen.blit(Parameters.bg_img, (x_pos, y_pos))
        # we make the image appear a second time
        Parameters.screen.blit(Parameters.bg_img, (Parameters.bg_width + x_pos, y_pos))

        if x_pos <= -Parameters.bg_width:
            Parameters.screen.blit(Parameters.bg_img, (Parameters.bg_width + x_pos, y_pos))
            x_pos = 0

        x_pos -= speedgame
        print(x_pos)

        # recording the commands from the player
        user_input = pygame.key.get_pressed()

        # calling the player:
        player.draw(Parameters.screen)
        player.update(user_input)

        # Making the obstacles appear
        # Randomly choosing the type of obstacle
        if len(obstacles) == 0:
            if random.randint(0, 1) == 0:
                obstacles.append(LargeCactus(
                    Parameters.LARGE_CACTUS, Parameters.WIDTH))
            elif random.randint(0, 2) == 1:
                obstacles.append(SmallCactus(
                    Parameters.SMALL_CACTUS, Parameters.WIDTH))
            else:
                obstacles.append(Bird(Parameters.BIRD, Parameters.WIDTH))

        for obstacle in obstacles:
            obstacle.draw(Parameters.screen)
            obstacle.update(speedgame, obstacles)

            if player.dino_rect.colliderect(obstacle.rect):

                pygame.time.delay(2000)
                Parameters.ifdead = True
                # menu(Parameters.ifdead)

        # drawing the clouds
        cloud.draw(Parameters.screen)
        cloud.update(speedgame, Parameters.WIDTH)

        score()  # we put at the end so it does not flash

        pygame.display.update()