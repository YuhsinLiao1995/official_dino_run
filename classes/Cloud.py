import pygame
from pygame.locals import *
import random
import os

IMAGE_PATH = "img/"

class Cloud:

  CLOUD = pygame.image.load(os.path.join(IMAGE_PATH, "1.Background/Cloud.png"))

  def __init__(self, width):
    self.x = width + random.randint(200, 500)
    print(self.x)
    self.y = random.randint(50, 200)
    self.image = self.CLOUD
    self.width = self.image.get_width()

  def update(self, speed, width):
    self.x -= speed
    if self.x < -self.width:
      self.x = width + random.randint(80, 1000)
      self.y = random.randint(50, 200)

  def draw(self, screen):
    screen.blit(self.image, (self.x, self.y))


class Weapon:

  WEAPON = pygame.image.load(os.path.join(
      IMAGE_PATH, "5. Weapons/Weapon1_Logo.png"))

  def __init__(self, width):
    self.x = width + random.randint(500, 1000)
    self.y = 100
    self.image = self.WEAPON
    self.width = self.image.get_width()
    self.rect = self.image.get_rect()
    self.rect.x = width*1.5
    self.rect.y = 380 - self.image.get_height()

  def update(self, speed, width):
    self.rect.x -= speed
    if self.rect.x < -self.width:
      self.rect.x = width + random.randint(300, 1000)
      self.rect.y = 150


  def draw(self, screen):
    screen.blit(self.image, (self.rect.x, self.rect.y))
    print(self.rect)
