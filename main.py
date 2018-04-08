# Tile Based Game
import pygame as pg
import sys
import random
from settings import *
from sprites import *


class Game:
    def __init__(self):
        # Initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.dt = None
        pg.key.set_repeat(500, 100)
        self.running = True

        # Running bool
        self.playing = True

        # Initialize sprite groups
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()

        # Set up Sprite Variables
        self.player = None


        # Load Data
        self.load_data()

    def load_data(self):
        pass

    def new(self):
        # Start a new game
        self.player = Player(self,0, 3)
        for x in range(10, 20):
            Wall(self, x, 5)

    def run(self):
        # Game loop
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        # Game Loop - Draw
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def events(self):
        # Game Loop - Events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT:
                    self.player.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.player.move(dx=1)
                if event.key == pg.K_UP:
                    self.player.move(dy=-1)
                if event.key == pg.K_DOWN:
                    self.player.move(dy=1)

    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        # game over/continue
        pass


g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.run()
    g.show_go_screen()
