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