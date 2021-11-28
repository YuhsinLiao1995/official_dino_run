import pygame
from global_parameters import Parameters


def menu():
    Parameters.isRunnung = True
    Parameters.screen = pygame.display.set_mode((Parameters.WIDTH, Parameters.HEIGHT))

    # while run:
    while Parameters.isRunnung:
        Parameters.screen.fill(Parameters.WHITE)

        font = pygame.font.Font("game_over.ttf", 90)
        fontTitle = pygame.font.Font("game_over.ttf", 110)

        if Parameters.isDead is False:
            text = font.render("Press any Key to Start", True, Parameters.FONT_COLOR)

        elif Parameters.isDead is True:

            textTitle = fontTitle.render(
                "Game Over YOU   LOSER!", True, Parameters.FONT_COLOR)
            textTitleRect = textTitle.get_rect()
            textTitleRect.center = (Parameters.WIDTH//2, Parameters.HEIGHT // 2 - 50)

            Parameters.scores.append(Parameters.point) #we add the score to listing of scores
            #print(Parameters.scores)
            text = font.render("Press any Key to Restart", True, Parameters.FONT_COLOR)
            score = font.render("Your Score: " + str(Parameters.point), True, Parameters.FONT_COLOR)
            scoreRect = score.get_rect()
            scoreRect.center = (Parameters.WIDTH // 2,Parameters.HEIGHT // 2 + 80)

            Parameters.screen.blit(score, scoreRect)
            Parameters.screen.blit(textTitle, textTitleRect)

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

