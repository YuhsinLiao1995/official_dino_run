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

class Sword(Gun):

    WEAPON = pygame.image.load(os.path.join(IMAGE_PATH, "5. Weapons/Weapon2.png"))
    WEAPON = pygame.transform.scale(WEAPON, (100, 100))




class Bullet:

    x_dino = 80
    y_dino = 320

    def __init__(self, width, dino_rect_y):
        BULLET1 = pygame.image.load(os.path.join(IMAGE_PATH, "5. Weapons/BulletBill1.png"))
        BULLET1 = pygame.transform.smoothscale(BULLET1, (50, 25))
        BULLET2 = pygame.image.load(os.path.join(IMAGE_PATH, "5. Weapons/BulletBill2.png"))
        BULLET2 = pygame.transform.smoothscale(BULLET2, (50, 25))
        BULLET3 = pygame.image.load(os.path.join(IMAGE_PATH, "5. Weapons/BulletBill3.png"))
        BULLET3 = pygame.transform.smoothscale(BULLET2, (50, 25))
        BULLET4 = pygame.image.load(os.path.join(IMAGE_PATH, "5. Weapons/BulletBill4.png"))
        BULLET4 = pygame.transform.smoothscale(BULLET2, (50, 25))
        self.shot_count = 0
        self.shotting_image = [BULLET1,BULLET2,BULLET3,BULLET4]
        self.image = self.shotting_image[0]
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.width = width
        self.type = 0
        self.rect = self.shotting_image[self.type].get_rect()
        self.rect.x = self.x_dino
        self.rect.y = dino_rect_y + 30
        self.isShooting = False


    def update(self, speed, bullets):
        if self.isShooting is True:
            #counting shot
            if self.shot_count > 3:
                self.shot_count = 0
            self.rect.x += speed*5
        if self.rect.x > self.width:
            bullets.pop()
            self.rect.x = 80

    def collide(self, speed):
        if self.isShooting is True:
            #counting shot
            if self.shot_count > 3:
                self.shot_count = 0
            self.rect.x += speed*2
            self.rect.x = 80

    def draw(self, screen):
        self.image = self.shotting_image[self.shot_count // 3]
        screen.blit(self.image, (self.rect.x, self.rect.y))
        self.shot_count += 1
        self.isShooting = True

