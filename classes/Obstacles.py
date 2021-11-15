import pygame
from pygame.locals import *
import random
import os

IMAGE_PATH = "img/"

#to improve with inheritance principles

class LargeCactus:
  def __init__(self, image, width):
    self.image = image
    self.type = random.randint(0, 2)
    self.rect = self.image[self.type].get_rect()
    self.rect.x = width*1.5
    self.rect.y = 380 - self.image[self.type].get_height()


  def update(self, speed, obstacles):
    self.rect.x -= speed
    if self.rect.x < -self.rect.width:
      obstacles.pop()

  def draw(self, screen):
    #print(self.rect.x)
    screen.blit(self.image[self.type], self.rect)


class SmallCactus:
  def __init__(self, image, width):
    self.image = image
    self.type = random.randint(0, 2)
    self.rect = self.image[self.type].get_rect()
    self.rect.x = width*1.5
    self.rect.y = 380 - self.image[self.type].get_height()

  def update(self, speed, obstacles):
    self.rect.x -= speed
    if self.rect.x < -self.rect.width:
      obstacles.pop()

  def draw(self, screen):
    #print(self.rect.x)
    screen.blit(self.image[self.type], self.rect)


class Bird:
  BIRD_HEIGHT = [250, 290, 300]

  def __init__(self, image, width):
    self.flap = 0
    self.image = image
    self.type = 0
    self.rect = self.image[self.type].get_rect()
    self.rect.x = width*1.5
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








