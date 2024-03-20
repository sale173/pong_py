import pygame
import sys

pygame.init()

WIDTH_CORT = 1200
HEIGHT_CORT = 800


line_color = (255, 255, 255)
line_start = (WIDTH_CORT // 2, 0)
line_end = (WIDTH_CORT // 2, HEIGHT_CORT)
line_WIDTH = 4

line_start_left = (0, 0)
line_end_left = (0, HEIGHT_CORT)

line_start_right = (WIDTH_CORT, 0)
line_end_right = (WIDTH_CORT, HEIGHT_CORT)

line_start_top = (0, 0)
line_end_top = (WIDTH_CORT, 0)

line_start_bot = (0, HEIGHT_CORT)
line_end_bot = (WIDTH_CORT, HEIGHT_CORT)

player_left_pos_x = 0
player_left_pos_y = 0

player_right_pos_x = WIDTH_CORT - 50
player_right_pos_y = 0

player_pos = pygame.Vector2(WIDTH_CORT, 0)

class Player_1:
    def __init__(self, pos_x, pos_y, width, height):
        self.pos_x = 0
        self.pos_y = 0
        self.width = 25
        self.height = 100

    def rect():
        pygame.draw.rect(screen, pos_x, pos_y, width)

class Player_2:

class Ball:


screen = pygame.display.set_mode((WIDTH_CORT, HEIGHT_CORT))
            
for i in range(HEIGHT_CORT):
    j = i + 6
    line_start = (WIDTH_CORT // 2, i)
    line_end = (WIDTH_CORT // 2, j)
    k = 1
    if i % 12 == 0:
        pygame.draw.line(screen, line_color, line_start, line_end, line_WIDTH)
    if k == 1:
        pygame.draw.line(screen, line_color, line_start_left, line_end_left, line_WIDTH)
        pygame.draw.line(screen, line_color, line_start_right, line_end_right, line_WIDTH)
        pygame.draw.line(screen, line_color, line_start_top, line_end_top, line_WIDTH)
        pygame.draw.line(screen, line_color, line_start_bot, line_end_bot, line_WIDTH)
        k += 1
            
player_rect_left = pygame.Rect(player_left_pos_x, player_left_pos_y, 50, 200)
player_rect_right = pygame.Rect(player_right_pos_x, player_right_pos_y, 50, 200)

pygame.draw.rect(screen, line_color, player_rect_left)
pygame.draw.rect(screen, line_color, player_rect_right)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
