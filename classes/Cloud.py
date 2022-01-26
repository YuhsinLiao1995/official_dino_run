import random
import os
import pygame

IMAGE_PATH = "img/"

class Cloud:

    CLOUD = pygame.image.load(os.path.join(IMAGE_PATH, "1.Background/Cloud.png"))

    def __init__(self, width):
        self.x = width + random.randint(200, 500)
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



