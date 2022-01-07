import random
import os
import pygame
import textwrap
from classes.Dino import Dino
from classes.Cloud import Cloud
from classes.Weapons import Gun, Sword, Bullet
from classes.Obstacles import LargeCactus, SmallCactus, Bird
from global_parameters import Parameters
# from attack import shot, cut

run = False
weaponCollected = []
cutting = False

def startRun():
    global speedgame, obstacles, weaponCollected, cutting
    # all variables
    Parameters.point = 0
    Parameters.isDead = False
    player = Dino(Parameters.themeOption, weaponCollected)
    cloud = Cloud(Parameters.WIDTH)
    gun = Gun(Parameters.WIDTH)
    sword = Sword(Parameters.WIDTH)

    pygame.display.set_icon(Parameters.logo)
    pygame.display.set_caption("Chrome Dino Runner")

    pygame.display.update()



    def score():
        global speedgame
        Parameters.point += 1
        font = pygame.font.Font("game_over.ttf", 70)

        text = font.render("Point: " + str(Parameters.point),
                           True, Parameters.FONT_COLOR)
        textRect = text.get_rect()
        (textRectx, textRecty) = (Parameters.WIDTH - 150, Parameters.HEIGHT // 4.5)
        textRect.center = (textRectx, textRecty)

        Parameters.screen.blit(text, textRect)
        pygame.display.update()
        if Parameters.point % 100 == 0:

          #make the game go faster
          speedgame += 1

    def showWeaponMenu(weaponList):
        font = pygame.font.Font("game_over.ttf", 70)

        # content = "No weapon" if weaponList == [] else if "gun" in
        content = ""
        if weaponList == []:
            content = "No weapon"
        else:
            if "gun" in weaponList:
                content = "Press S to shot"
            if "sword" in weaponList:
                content = "Press C to attack"
            if "gun" in weaponList and "sword" in weaponList:
                content = "Press S to shot\nPress C to attack"



        text = font.render(content,True, Parameters.FONT_COLOR)
        textRect = text.get_rect()
        (textRectx, textRecty) = (Parameters.WIDTH/5.5, Parameters.HEIGHT // 5)
        textRect.center = (textRectx, textRecty)

        Parameters.screen.blit(text, textRect)
        pygame.display.update()

    #we load the correct background
    options = ["Dino", "Pika", "Mario"]
    path = "img/1.Background/" + options[Parameters.themeOption - 1] + ".png"
    bg_img = pygame.image.load(path)
    bg_size = (bg_width, bg_height) = (bg_img.get_width(),
                                       bg_img.get_height())

    # displaying the background # coordinates of the background
    img_coordinates = (x_pos, y_pos) = (0, 0)
    Parameters.screen.blit(bg_img, (x_pos, y_pos))
    Parameters.screen.blit(
        bg_img, (x_pos + bg_width, y_pos))

    # making the game run
    global run
    run = True
    speedgame = 10  # speed at which the background will move
    print(speedgame)

    # managing obstacles
    obstacles = []

    # managing bullets
    bullets = []
    bulletsCount = 0

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

    clock = pygame.time.Clock()

    while run:

        clock.tick(120)


        # we make the run possible to quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                run = False
                paused()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s and "gun" in weaponCollected:
                bullets.append(Bullet(Parameters.WIDTH,player.dino_rect.y))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c and "sword" in weaponCollected:
                cutting = True


        # we make the background loop
        # we color the rest of the background in white
        Parameters.screen.fill(Parameters.WHITE)
        # we make the image appear one time
        Parameters.screen.blit(bg_img, (x_pos, y_pos))
        # we make the image appear a second time
        Parameters.screen.blit(
            bg_img, (bg_width + x_pos, y_pos))

        if x_pos <= -bg_width:
            Parameters.screen.blit(
                bg_img, (bg_width + x_pos, y_pos))
            x_pos = 0

        x_pos -= speedgame

        # recording the commands from the player
        user_input = pygame.key.get_pressed()

        # drawing the clouds
        cloud.draw(Parameters.screen)
        cloud.update(speedgame, Parameters.WIDTH)



        # calling the player:
        player.draw(Parameters.screen)
        player.update(user_input)

        # Making the obstacles appear
        # Randomly choosing the type of obstacle
        if len(obstacles) == 0:
            if random.randint(0, 1) == 0:
                obstacles.append(LargeCactus(
                    Parameters.WIDTH, Parameters.themeOption))
            elif random.randint(0, 2) == 1:
                obstacles.append(SmallCactus(
                    Parameters.WIDTH, Parameters.themeOption))
            else:
                obstacles.append(Bird(Parameters.WIDTH, Parameters.themeOption))

        for obstacle in obstacles:
            obstacle.draw(Parameters.screen)
            obstacle.update(speedgame, obstacles)

            #making the collision with obstacle lethal
            if player.dino_rect.colliderect(obstacle.rect):
                # print("obstacle.rect", obstacle.rect)
                if cutting:
                    obstacle.update(speedgame, obstacles.remove(obstacle))
                    cutting = False
                else:
                    #pygame.time.delay(2000)
                    Parameters.isDead = True
                    weaponCollected = []
                    return Parameters.isDead
                    # menu(Parameters.ifdead)

                        #drawing the weapon
            for bullet in bullets:
                bullet.draw(Parameters.screen)
                bullet.update(speedgame, bullets)
                bulletsCount += 1
                if bulletsCount >= 5:
                    bulletsCount = 0
                    if "gun" in weaponCollected:
                        weaponCollected.remove('gun')

                if obstacle.rect.colliderect(bullet.rect):
                    obstacle.update(speedgame, obstacles.remove(obstacle))
                    bullets.remove(bullet)
                    bullet.collide(speedgame)


        if "gun" not in weaponCollected and Parameters.point >= 1000:
            gun.draw(Parameters.screen)
            gun.update(speedgame, Parameters.WIDTH)

        if "sword" not in weaponCollected and Parameters.point >= 500:
            sword.draw(Parameters.screen)
            sword.update(speedgame, Parameters.WIDTH)

        if player.dino_rect.colliderect(gun.rect) and "gun" not in weaponCollected:

            weaponCollected.append("gun")

        if player.dino_rect.colliderect(sword.rect) and "sword" not in weaponCollected:
        #    global weaponCollected
            weaponCollected.append("sword")


        showWeaponMenu(weaponCollected)
        score()  # we put at the end so it does not flash

        pygame.display.update()
