import pygame
from global_parameters import Parameters


pygame.font.init()
font = pygame.font.Font("freesansbold.ttf", 30)
fontTitle = pygame.font.Font("freesansbold.ttf", 50)
fontButton = pygame.font.SysFont("Arial", 23)

def button(i, x, y, w, h, img, title):
    pygame.font.init()

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    buttonTitle = fontButton.render(title, False, (0, 0, 0))
    img = pygame.transform.scale(img, (w, h))
    Parameters.screen.blit(img, (x, y))
    Parameters.screen.blit(buttonTitle, (x, y+50))

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        if click[0] == 1:
            Parameters.themeOption = i

def menu():
    run = True
    Parameters.screen = pygame.display.set_mode((Parameters.WIDTH, Parameters.HEIGHT))
    pygame.display.update()


<<<<<<< HEAD
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

=======
    while run:
        Parameters.screen.fill(Parameters.WHITE)

        if Parameters.isDead is False:

            title = fontTitle.render("Welcome to the CUTE DINO", True, (0, 0, 0))
            titleRect = title.get_rect()
            titleRect.center = (Parameters.WIDTH//2, Parameters.HEIGHT // 3- 40)
            Parameters.screen.blit(title, titleRect)

            text = font.render("Choose a theme to start the game", True, (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (Parameters.WIDTH//2, Parameters.HEIGHT // 3 + 50)
            Parameters.screen.blit(text, textRect)

        elif Parameters.isDead is True:
            Parameters.themeOption = 0
            title = fontTitle.render("Game Over...", True, (0, 0, 0))
            titleRect = title.get_rect()
            titleRect.center = (Parameters.WIDTH//2, Parameters.HEIGHT // 3- 50)
            Parameters.screen.blit(title, titleRect)

            text = font.render("Choose a theme to restart the game", True, (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (Parameters.WIDTH//2, Parameters.HEIGHT // 2)
            Parameters.screen.blit(text, textRect)

            score = font.render("Your Score: " + str(Parameters.point), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (Parameters.WIDTH // 2, Parameters.HEIGHT // 2 - 60)
>>>>>>> 757069d6e393d5bd5b8ef25bea31dd735dea6915
            Parameters.screen.blit(score, scoreRect)
            Parameters.screen.blit(textTitle, textTitleRect)

        button(1, Parameters.WIDTH/2 - 200, 290, 50, 50,
               pygame.image.load("img/4. ThemeButton/themeDino.png"), "Dino")
        button(2, Parameters.WIDTH/2 - 50, 290, 50, 50,
               pygame.image.load("img/4. ThemeButton/themePicachu.jpeg"), "Picachu")
        button(3, Parameters.WIDTH/2 + 100, 290, 50, 50,
               pygame.image.load("img/4. ThemeButton/themeMario.jpeg"), "Mario")

        pygame.display.update()

        for event in pygame.event.get():

            if Parameters.firstTime is True:


                if event.type == pygame.QUIT:
                    Parameters.isRunnung = False
                    pygame.display.quit()
                    pygame.quit()
                    exit()

                if Parameters.themeOption != 0:
                    Parameters.isRunnung = True
                    Parameters.firstTime = False
                    return Parameters.isRunnung


            elif Parameters.firstTime is False:

                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    exit()

                if Parameters.themeOption != 0:
                    Parameters.isDead = False
                    Parameters.isRunnung = True
                    Parameters.point = 0
                    return Parameters.isRunnung
