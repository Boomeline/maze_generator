import pygame as pg

class Player ():
    def __init__(self, cellSize : int):
        self.x, self.y = 0, 0
        self.cellSize = cellSize

    def move(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.y -= self.cellsize
                if event.key == pg.K_DOWN:
                    self.y += self.cellsize
                if event.key == pg.K_LEFT:
                    self.X -= self.cellsize
                if event.key == pg.K_RIGHT:
                    self.X += self.cellsize  

    def check_walls(self):
        pass

    def check_green(self):
        pass