import pygame
import random

pygame.init()

# размеры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# название экрана
pygame.display.set_caption("Игра ТИР")

# иконка
icon = pygame.image.load("image/openmidj6_logo_shooting_gallery_cdbb2e40-f6bf-411f-b6ea-545a52ccd5a6.png")
pygame.display.set_icon(icon)

# цель - куда стрелять будем
target_image =  pygame.image.load("image/alarm_clock_fotor.png")
# размер изображения
target_width = 50
target_heigth = 50

# случайные координаты для изображения
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_heigth)

# цвет для заливки экрана
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255) )

running = True
while running:
    pass

pygame.quit()
