import pygame
from pygame.locals import *
import random
import os

IMAGE_PATH = "img/"

class Weapon:

  WEAPON = pygame.image.load(os.path.join(IMAGE_PATH, "5. Weapons/Weapon1_Logo.png"))

  def __init__(self, width):
    self.x = width + random.randint(500, 1000)
    print(self.x)
    self.y = 150
    self.image = self.WEAPON
    self.width = self.image.get_width()

  def update(self, speed, width):
    self.x -= speed
    if self.x < -self.width:
      self.x = width + random.randint(300, 1000)
      self.y = 150

  def draw(self, screen):
    screen.blit(self.image, (self.x, self.y))
