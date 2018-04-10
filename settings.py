import pygame as pg


# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)

# Game options / settings
TITLE = "Tilemap Demo"
WIDTH = 1024
HEIGHT = 768
FPS = 60
BGCOLOR = BROWN

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

WALL_IMG = "tileGreen_39.png"

# Player settings
PLAYER_SPEED = 300
PLAYER_ROT_SPEED = 250
PLAYER_IMG = "manBlue_gun.png"
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)


# MOB settings
MOB_IMG = "zombie1_hold.png"
