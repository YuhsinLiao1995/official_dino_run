import pygame
from classes.Dino import Dino
from classes.Cloud import Cloud
from classes.Obstacles import LargeCactus, SmallCactus, Bird
from pygame.locals import *
import random
import os


#Defining the constants
WINDOW_SIZE = (WIDTH, HEIGHT) = (1000, 500)

#colors variables
BLACK = (0, 0, 0)
WHITE = (247, 247, 247)
FONT_COLOR = (83, 83, 83)

IMAGE_PATH = "img/"

SMALL_CACTUS = [
    pygame.image.load(os.path.join(
        IMAGE_PATH, "3. Obstacles/SmallCactus1.png")),
    pygame.image.load(os.path.join(
        IMAGE_PATH, "3. Obstacles/SmallCactus2.png")),
    pygame.image.load(os.path.join(
        IMAGE_PATH, "3. Obstacles/SmallCactus3.png")),
]

LARGE_CACTUS = [
    pygame.image.load(os.path.join(
        IMAGE_PATH, "3. Obstacles/LargeCactus1.png")),
    pygame.image.load(os.path.join(
        IMAGE_PATH, "3. Obstacles/LargeCactus2.png")),
    pygame.image.load(os.path.join(
        IMAGE_PATH, "3. Obstacles/LargeCactus3.png")),
]

BIRD = [
  pygame.image.load(os.path.join(IMAGE_PATH, "3. Obstacles/Bird1.png")),
  pygame.image.load(os.path.join(IMAGE_PATH, "3. Obstacles/Bird2.png"))
]


def main():
  global speedgame, obstacles, screen
  pygame.init()
  #all variables
  player = Dino()
  cloud = Cloud(WIDTH)

  #screen and background settings
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  bg_img = pygame.image.load("img/1.Background/track_bis.png") #load the track image
  bg_size = (bg_width, bg_height) = (bg_img.get_width(), bg_img.get_height()) #getting the track image size

  #implementing the logo and caption of the game
  logo = pygame.image.load(os.path.join(IMAGE_PATH, "1.Background/Logo.png"))
  pygame.display.set_icon(logo)
  pygame.display.set_caption("Chrome Dino Runner")

  #displaying the background
  img_coordinates = (x_pos, y_pos) = (0, HEIGHT - 5*bg_height) #coordinates of the background
  screen.blit(bg_img, (x_pos, y_pos))
  screen.blit(bg_img, (x_pos + bg_width, y_pos))

  #making the game run
  run = True
  speedgame = 10 #speed at which the background will move
  pause = False

  #managing obstacles
  obstacles = []

  #managing pause and unpause
  def paused():
    pause = True
    font = pygame.font.Font("game_over.ttf", 90)
    text = font.render("Game Paused, Press 'u' to Unpause", True, FONT_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (WIDTH//2, HEIGHT//3)
    screen.blit(text, text_rect)
    pygame.display.flip()

    while pause:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_u:
          pause = False
          run = True

  def unpause():
    print("we want to unpause")
    pause = False
    run = True

  while run:

    #we make the run possible to quit:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        pygame.display.quit()
        exit()
      if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
        run = False
        paused()


    #we make the background loop
    screen.fill(WHITE) #we color the rest of the background in white
    screen.blit(bg_img, (x_pos, y_pos)) #we make the image appear one time
    screen.blit(bg_img, (bg_width + x_pos, y_pos)) #we make the image appear a second time

    if x_pos <= -bg_width:
      screen.blit(bg_img, (bg_width + x_pos, y_pos))
      x_pos = 0

    x_pos -= speedgame



    #recording the commands from the player
    user_input = pygame.key.get_pressed()

    #calling the player:
    player.draw(screen)
    player.update(user_input)

    #Making the obstacles appear
    #Randomly choosing the type of obstacle
    if len(obstacles) ==0:
      if random.randint(0, 1) == 0:
        obstacles.append(LargeCactus(LARGE_CACTUS, WIDTH))
      elif random.randint(0, 2) == 1:
        obstacles.append(SmallCactus(SMALL_CACTUS, WIDTH))
      else:
        obstacles.append(Bird(BIRD, WIDTH))

    #drawing the obstacles in the window
    for obstacle in obstacles:
      obstacle.draw(screen)
      obstacle.update(speedgame, obstacles)

    #drawing the clouds
    cloud.draw(screen)
    cloud.update(speedgame, WIDTH)



    pygame.display.update()

#calling the game
main()

