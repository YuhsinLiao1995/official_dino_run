import random
import pygame
from classes.Dino import Dino
from classes.Cloud import Cloud
from classes.Obstacles import LargeCactus, SmallCactus, Bird
import os
from global_parameters import Parameters
import datetime


def startRun():
    global speedgame, obstacles, points
    # all variables
    points = 0
    Parameters.isDead = False
    player = Dino()
    cloud = Cloud(Parameters.WIDTH)

    pygame.display.set_icon(Parameters.logo)
    pygame.display.set_caption("Chrome Dino Runner")

    # making the game run
    global run
    run = True
    speedgame = 10  # speed at which the background will move

    # managing obstacles
    obstacles = []

    def score():
        global  speedgame, points
        points += 1
        # making gamespeed goes faster based on points accumulation
        if points % 100 == 0:
            speedgame += 1

        font = pygame.font.Font("game_over.ttf", 70)
        text = font.render("Point: " + str(points), True, Parameters.FONT_COLOR)
        textRect = text.get_rect()
        textRect.center = (Parameters.WIDTH - 150, Parameters.HEIGHT // 4.5)
        Parameters.screen.blit(text, textRect)
        pygame.display.update()

    # displaying the background
    img_coordinates = (x_pos, y_pos) = (
        0, Parameters.HEIGHT - 5*Parameters.bg_height)  # coordinates of the background
    Parameters.screen.blit(Parameters.bg_img, (x_pos, y_pos))
    Parameters.screen.blit(Parameters.bg_img, (x_pos + Parameters.bg_width, y_pos))


    # managing pause and unpause
    def paused():
        global run
        pause = True
        font = pygame.font.Font("game_over.ttf", 90)
        text = font.render("Game Paused, Press 'r' to Resume",
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
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    run = True
                    pause = False

    while run:

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
                Parameters.isDead = True
                return Parameters.isDead
                # menu(Parameters.ifdead)

            # if player.dino_rect.colliderect(obstacle.rect):
            #     pygame.time.delay(2000)
            #     death_count += 1
            #     menu(death_count)

        # drawing the clouds
        cloud.draw(Parameters.screen)
        cloud.update(speedgame, Parameters.WIDTH)

        score()  # we put at the end so it does not flash

        pygame.display.update()
