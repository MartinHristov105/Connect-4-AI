import pygame
import numpy
import sys
import math
import random

# Board dimensions.
COLUMN = 10
ROW = 10
RECT = 50
RAD = int(RECT / 2 - 5)

# Colors.
BLUE = (52, 186, 235)
GREY = (70, 71, 70)
WHITE = (255,255,255)
BLACK = (0,0,0)
YELLOW = (230,230,20)

# Players.
PLAYER = 1
AI = 2

# Value of checkers.
EMPTY = 0
PLAYER_PIECE = 1
AI_PIECE = 2

# Number of consecutive checkers to win.
WINDOW = 4

# Screen sizes.
WIDTH = COLUMN * RECT
HEIGHT = (ROW + 1) * RECT
SIZE = (WIDTH, HEIGHT)

# Font.
pygame.init()
SCREEN = pygame.display.set_mode(SIZE)
WINNER = pygame.font.SysFont("arialblack", 25)