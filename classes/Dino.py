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

  #dino images
  RUNNING = [pygame.image.load(os.path.join(IMAGE_PATH, "2. Dino/DinoRun1.png")),
             pygame.image.load(os.path.join(IMAGE_PATH, "2. Dino/DinoRun2.png"))]

  DUCKING = [pygame.image.load(os.path.join(IMAGE_PATH, "2. Dino/DinoDuck1.png")),
             pygame.image.load(os.path.join(IMAGE_PATH, "2. Dino/DinoDuck2.png"))]

  JUMPING = pygame.image.load(os.path.join(IMAGE_PATH, "2. Dino/DinoJump.png"))

  #initializing our dino
  def __init__(self):
    #regarding the image of the dino
    self.running_image = self.RUNNING
    self.jumping_image = self.JUMPING
    self.ducking_image = self.DUCKING
    self.image = self.running_image[0]  # first image of the dino

    #regarding the position of the dino
    self.dino_rect = self.image.get_rect()
    self.dino_rect.x = self.x_dino
    self.dino_rect.y = self.y_dino

    #regarding the action of the dino - actions booleans
    self.is_jumping = False
    self.is_running = True
    self.is_ducking = False

    #action count
    self.run_count = 0
    self.vel = self.jump_vel

  #running function
  def run(self):
    # vary from image 1 and image 2
    self.image = self.running_image[self.run_count // 10]
    self.dino_rect.x = self.x_dino
    self.dino_rect.y = self.y_dino
    self.run_count += 1

  #ducking function
  def duck(self):
    self.image = self.ducking_image[self.run_count // 10]
    self.dino_rect.x = self.x_dino
    self.dino_rect.y = self.y_dino_duck
    self.run_count += 1

  #jumping function
  def jump(self):
    self.image = self.JUMPING  # replace the running image witht the jumping image
    #print("START", self.y_dino)
    if self.is_jumping:
      self.dino_rect.y -= (self.vel * abs(self.vel)) * 0.25  # make the dino move on the y axis
      self.vel -= 0.5  # enable the dino to go back down -- make the dino go higher or lower
      #print("JUMPING", self.y_dino, self.vel, self.is_jumping)

    if self.vel < -self.jump_vel:  # once the dino is back at his original y level, we put all the parameters to their normal value
      #print("BOUM", self.y_dino)
      self.is_jumping = False
      self.vel = self.jump_vel
      #print("BOUM", self.y_dino)


  #updating variables and images
  def update(self, user_input):
    #updating action booleans
    if self.is_running:
      self.run()
    if self.is_ducking:
      self.duck()
    if self.is_jumping:
      self.jump()

    #counting steps
    if self.run_count > 19:
      self.run_count = 0

    if not self.is_jumping:
      if (user_input[pygame.K_UP] or user_input[pygame.K_SPACE]) and self.dino_rect.y == self.y_dino:
        self.is_running = False
        self.is_ducking = False
        self.is_jumping = True
      elif user_input[pygame.K_DOWN]:
        self.is_running = False
        self.is_ducking = True
        self.is_jumping = False
      else:
        self.is_jumping = False
        self.is_ducking = False
        self.is_running = True


  #displaying the dino corresponding to each action

  def draw(self, screen):
    screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
