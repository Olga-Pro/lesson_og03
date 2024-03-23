import pygame

pygame.init()

# размеры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# название экрана
pygame.display.set_caption("Игра ТИР")

# иконка
icon = pygame.image.load("")
running = True
while running:
    pass

pygame.quit()
