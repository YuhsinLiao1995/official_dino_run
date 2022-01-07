import pygame
from pygame.locals import *
import os

IMAGE_PATH = "img/"

class Dino:
    #dino constants
    x_dino = 80
    y_dino = 290
    y_dino_duck = 320
    jump_vel = 10
    option = 0

    #dino images

    #initializing our dino
    def __init__(self, option, weaponList):
        #regarding the image of the dino
        self.option = option
        self.weaponList = weaponList
        #select correct folder
        options = ["Dino", "Pika", "Mario"]
        img_path= "img/2. Dino/" + options[option - 1]
        self.running_image = [pygame.image.load(img_path+"/Run1.png"),
                              pygame.image.load(img_path+"/Run2.png"),
                              pygame.image.load(img_path+"/Run3.png"),
                              pygame.image.load(img_path+"/Run4.png")]
        self.jumping_image = pygame.image.load(img_path+"/Jump.png")
        self.ducking_image = [pygame.image.load(img_path+"/Duck1.png"),
                              pygame.image.load(img_path+"/Duck2.png"),
                              pygame.image.load(img_path+"/Duck3.png"),
                              pygame.image.load(img_path+"/Duck4.png")]
        self.image = self.running_image[0]  # first image of the dino
        ## update shotting img
        self.shotting_image = [pygame.image.load(img_path+"/Shot1.png"),
                              pygame.image.load(img_path+"/Shot2.png")]


        ## update cutting img
        self.cutting_image = [pygame.image.load(img_path+"/Stab1.png"),
                              pygame.image.load(img_path+"/Stab2.png")]

        #regarding the position of the dino
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_dino
        self.dino_rect.y = self.y_dino

        #regarding the action of the dino - actions booleans
        self.is_jumping = False
        self.is_running = True
        self.is_ducking = False
        self.is_shotting = False
        self.is_cutting = False

        self.is_jumpping_and_cutting = False
        self.is_jumpping_and_shotting = False

        #action count
        self.run_count = 0
        self.vel = self.jump_vel
        self.shot_count = 0
        self.cut_count = 0

    #running function
    def run(self):
        # vary from image 1 and image 2
        self.image = self.running_image[self.run_count // 5]
        self.dino_rect.x = self.x_dino
        self.dino_rect.y = self.y_dino
        self.run_count += 1

    #ducking function
    def duck(self):
        self.image = self.ducking_image[self.run_count // 5]
        self.dino_rect.x = self.x_dino
        self.dino_rect.y = self.y_dino_duck
        self.run_count += 1

    #jumping function
    def jump(self):
        # replace the running image witht the jumping image
        options = ["Dino", "Pika", "Mario"]
        img_path = "img/2. Dino/" + options[self.option - 1]

        if self.is_jumpping_and_shotting:
            self.image = pygame.image.load(img_path+"/Shot1.png")
        elif self.is_jumpping_and_cutting:
            self.image = pygame.image.load(img_path+"/Stab1.png")
        else:
            pygame.image.load(img_path+"/Jump.png")

        if self.is_jumping :
            # make the dino move on the y axis
            self.dino_rect.y -= (self.vel * abs(self.vel)) * 0.25
            # enable the dino to go back down -- make the dino go higher or lower
            self.vel -= 0.5

        # once the dino is back at his original y level, we put all the parameters to their normal value
        if self.vel < -self.jump_vel:
            self.is_jumping = False
            self.vel = self.jump_vel



    # cut function
    def cut(self):
        # replace the image witht the cutting image
        options = ["Dino", "Pika", "Mario"]
        img_path = "img/2. Dino/" + options[self.option - 1]
        if self.is_cutting:
            # vary from image 1 to image 4
            self.image = self.cutting_image[self.cut_count // 2]
            self.dino_rect.x = self.x_dino
            self.dino_rect.y = self.y_dino
            self.cut_count += 1

    #shot function
    def shot(self):
         # replace the image witht the shotting image
        options = ["Dino", "Pika", "Mario"]
        img_path = "img/2. Dino/" + options[self.option - 1]
        if self.is_shotting:
            # vary from image 1 to image 4
            self.image = self.shotting_image[self.shot_count // 2]
            self.dino_rect.x = self.x_dino
            self.dino_rect.y = self.y_dino
            self.shot_count += 1


    #updating variables and images
    def update(self, user_input):
        #updating action booleans
        if self.is_running:
            self.run()
        if self.is_ducking:
            self.duck()
        if self.is_jumping:
            self.jump()
        if self.is_shotting:
            self.shot()
        if self.is_cutting:
            self.cut()


        #counting steps
        if self.run_count > 19:
            self.run_count = 0
        #counting shot
        if self.shot_count > 3:
            self.shot_count = 0
        #counting cut
        if self.cut_count > 3:
            self.cut_count = 0

        if not self.is_jumping :
            if user_input[pygame.K_s] and user_input[pygame.K_SPACE] and "gun" in self.weaponList and self.dino_rect.y == self.y_dino:
                self.is_running = False
                self.is_ducking = False
                self.is_jumping = True
                self.is_shotting = False
                self.is_cutting = False
                self.is_jumpping_and_shotting = True
                self.is_jumpping_and_cutting = False
            elif user_input[pygame.K_c] and user_input[pygame.K_SPACE] and "sword" in self.weaponList and self.dino_rect.y == self.y_dino:
                self.is_running = False
                self.is_ducking = False
                self.is_jumping = True
                self.is_shotting = False
                self.is_cutting = False
                self.is_jumpping_and_shotting = False
                self.is_jumpping_and_cutting = True
            elif (user_input[pygame.K_UP] or user_input[pygame.K_SPACE]) and self.dino_rect.y == self.y_dino:
                self.is_running = False
                self.is_ducking = False
                self.is_jumping = True
                self.is_shotting = False
                self.is_cutting = False
                self.is_jumpping_and_shotting = False
                self.is_jumpping_and_cutting = False
            elif user_input[pygame.K_DOWN]:
                self.is_running = False
                self.is_ducking = True
                self.is_jumping = False
                self.is_shotting = False
                self.is_cutting = False
                self.is_jumpping_and_shotting = False
                self.is_jumpping_and_cutting = False
            elif user_input[pygame.K_s] and "gun" in self.weaponList:
                self.is_running = False
                self.is_ducking = False
                self.is_jumping = False
                self.is_shotting = True
                self.is_cutting = False
                self.is_jumpping_and_shotting = False
                self.is_jumpping_and_cutting = False
            elif user_input[pygame.K_c] and "sword" in self.weaponList:
                self.is_running = False
                self.is_ducking = False
                self.is_jumping = False
                self.is_shotting = False
                self.is_cutting = True
                self.is_jumpping_and_shotting = False
                self.is_jumpping_and_cutting = False
            else:
                self.is_jumping = False
                self.is_ducking = False
                self.is_running = True
                self.is_shotting = False
                self.is_cutting = False
                self.is_jumpping_and_shotting = False
                self.is_jumpping_and_cutting = False


  #displaying the dino corresponding to each action

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
