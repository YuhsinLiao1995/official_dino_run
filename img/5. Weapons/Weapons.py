import pygame
from classes.Dino import Dino
from pygame.locals import *
import random
import os

IMAGE_PATH = "img/"


class Gun:

  WEAPON = pygame.image.load(os.path.join(
      IMAGE_PATH, "5. Weapons/Weapon1.png"))
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
    print(self.rect)

class Sword(Gun):

  WEAPON = pygame.image.load(os.path.join(
      IMAGE_PATH, "5. Weapons/Weapon2.png"))
  WEAPON = pygame.transform.scale(WEAPON, (100, 100))


class Bullet:
  BIRD_HEIGHT = [250, 290, 300]

  def __init__(self, width, option):
    self.flap = 0
    self.image = [pygame.image.load("5. Weapons/BulletBill1.png"),
                              pygame.image.load("5. Weapons/BulletBill2.png"),
                              pygame.image.load("5. Weapons/BulletBill3.png"),
                              pygame.image.load("5. Weapons/BulletBill4.png")]
    # if option == 1:
    #   self.image = [
    #       pygame.image.load(os.path.join(
    #           IMAGE_PATH, "3. Obstacles/Bird1.png")),
    #       pygame.image.load(os.path.join(
    #           IMAGE_PATH, "3. Obstacles/Bird2.png")),
    #   ]
    # elif option == 2:
    #   self.image = [
    #       pygame.image.load(os.path.join(
    #           IMAGE_PATH, "3. Obstacles/FlyingPoke1.png")),
    #       pygame.image.load(os.path.join(
    #           IMAGE_PATH, "3. Obstacles/FlyingPoke2.png")),
    #   ]
    # else:
    #   self.image = [
    #       pygame.image.load(os.path.join(
    #           IMAGE_PATH, "3. Obstacles/BulletBill1.png")),
    #       pygame.image.load(os.path.join(
    #           IMAGE_PATH, "3. Obstacles/BulletBill2.png")),
    #   ]
    self.type = 0
    self.rect = self.image[self.type].get_rect()
    self.rect.x = width
    self.rect.y = random.choice(self.BIRD_HEIGHT)

  def update(self, speed, obstacles):
    self.rect.x -= speed
    if self.rect.x < -self.rect.width:
      obstacles.pop()

  def draw(self, screen):
    #print(self.flap )
    if self.flap >= 17:
      self.flap = 0
    screen.blit(self.image[self.flap //9], self.rect)
    self.flap += 1
    print("bird:", self.rect)

#   def __init__(self, width):
#     self.x = width + random.randint(500, 1000)
#     self.y = 100
#     self.image = self.WEAPON
#     self.width = self.image.get_width()
#     self.rect = self.image.get_rect()
#     self.rect.x = width*1.5
#     self.rect.y = 380 - self.image.get_height()

#   def update(self, speed, width):
#     self.rect.x -= speed
#     if self.rect.x < -self.width:
#       self.rect.x = width + random.randint(300, 1000)
#       self.rect.y = 150


#   def draw(self, screen):
#     screen.blit(self.image, (self.rect.x, self.rect.y))
#     print(self.rect)


