import pygame
from global_parameters import Parameters


def menu():
    Parameters.isRunnung = True
    Parameters.screen = pygame.display.set_mode((Parameters.WIDTH, Parameters.HEIGHT))

    # while run:
    while Parameters.isRunnung:
        Parameters.screen.fill(Parameters.WHITE)

        font = pygame.font.Font("freesansbold.ttf", 30)

        if Parameters.isDead is False:
            text = font.render("Press any Key to Start", True, (0, 0, 0))

        elif Parameters.isDead is True:
            text = font.render("Press any Key to Restart", True, (0, 0, 0))
            score = font.render("Your Score: " + str(Parameters.point), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (Parameters.WIDTH // 2, Parameters.HEIGHT // 2 + 50)
            Parameters.screen.blit(score, scoreRect)

        textRect = text.get_rect()
        textRect.center = (Parameters.WIDTH//2, Parameters.HEIGHT // 2)
        Parameters.screen.blit(text, textRect)
        pygame.display.update()

        for event in pygame.event.get():

            if Parameters.firstTime is True:

                if event.type == pygame.QUIT:
                    Parameters.isRunnung = False
                    pygame.display.quit()
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    Parameters.isRunnung = True
                    Parameters.firstTime =False
                    return Parameters.isRunnung

            elif Parameters.firstTime is False:

                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    Parameters.isDead = False
                    Parameters.point = 0
                    Parameters.isRunnung = False

