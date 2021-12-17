import pygame
from classes.Dino import Dino
from pygame.locals import *
import random
import os

IMAGE_PATH = "img/"

class Gun:

  GUN = pygame.image.load(os.path.join(IMAGE_PATH, "5. Weapons/Weapon1.png"))

  def __init__(self, width, dino):
    self.x = 80
    print(self.x)
    self.y = dino
    self.image = self.GUN
    self.width = self.image.get_width()
    self.rect = self.image.get_rect()
    self.rect.x = self.x #must be the same as self.x in Dino to enable collision
    self.rect.y = self.y

  def update(self, speed, width):
    self.rect.x -= speed
    if self.rect.x < -self.rect.width:
      self.rect.x = width + random.randint(300, 1000)
      self.y = 150

  def draw(self, screen):
    screen.blit(self.image, (self.x, self.y))