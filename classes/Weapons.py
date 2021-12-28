import pygame
from pygame.locals import *
import random
import os

IMAGE_PATH = "img/"


class Gun:

    WEAPON = pygame.image.load(os.path.join(IMAGE_PATH, "5. Weapons/Weapon1.png"))
    WEAPON = pygame.transform.scale(WEAPON, (100, 30))
    def __init__(self, width):
        self.x = width + random.randint(500, 1000)
        self.y = 100
        self.image = self.WEAPON
        self.width = self.WEAPON.get_width()
        self.rect = self.image.get_rect()
        self.rect.x = width*1.5
        self.rect.y = 380 - self.image.get_height()

    def update(self, speed, width, taken = False):
        self.rect.x -= speed
        if self.rect.x < -self.width and taken is False:
            self.rect.x = width + random.randint(300, 1000)
            self.rect.y = 150


    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        # print(self.rect)

class Sword(Gun):

    WEAPON = pygame.image.load(os.path.join(IMAGE_PATH, "5. Weapons/Weapon2.png"))
    WEAPON = pygame.transform.scale(WEAPON, (100, 100))

class Bullet:
    # BIRD_HEIGHT = [250, 290, 300]

    def __init__(self):
        self.shot_count = 0
        self.shotting_image = [pygame.image.load(os.path.join(IMAGE_PATH, "5. Weapons/BulletBill1.png")),
                              pygame.image.load(os.path.join(IMAGE_PATH, "5. Weapons/BulletBill2.png")),
                              pygame.image.load(os.path.join(IMAGE_PATH, "5. Weapons/BulletBill3.png")),
                              pygame.image.load(os.path.join(IMAGE_PATH, "5. Weapons/BulletBill4.png"))]
        self.image = self.shotting_image[0]
        self.width = self.shotting_image[0].get_width()
        self.type = 0
        self.rect = self.shotting_image[self.type].get_rect()
        self.rect.x = 80
        self.rect.y = 200

    def update(self, speed, user_input):
        if user_input[pygame.K_s]:
            #counting shot
            if self.shot_count > 3:
                self.shot_count = 0
            self.rect.x += speed
            print("speed", speed)

        # if self.rect.x < -self.rect.width:
        #     obstacles.pop()

    def draw(self, screen, user_input):

        # if self.flap >= 17:
        #     self.flap = 0
        if user_input[pygame.K_s]:
            self.image = self.shotting_image[self.shot_count // 3]
            screen.blit(self.image, (self.rect.x, self.rect.y))
            self.shot_count += 1
            # print("speed", speed)
            print("bulllllllet:", self.rect.x)
