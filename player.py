import pygame as pg

class Player ():
    def __init__(self, cellSize : int, grid_size ):
        self.x, self.y = 0, 30
        self.cellSize = cellSize
        self.gridSize = grid_size 

    def drawPlayer(self, screen):
        pg.draw.rect(screen, (255, 0, 0), (self.x, self.y, 15, 15)) 
        pass

    def move(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.y -= self.cellSize
                if event.key == pg.K_DOWN:
                    self.y += self.cellSize
                if event.key == pg.K_LEFT:
                    self.x -= self.cellSize
                if event.key == pg.K_RIGHT:
                    self.x += self.cellSize  

    def check_walls(self, neighbors):
        for neighbor in neighbors:
            for wall_n in neighbor.walls:
                wall = neighbors.walls[wall_n]
                if not wall:

                    pass

    def checkGreen(self, cells: list):
        indexX = self.x/self.gridSize
        indexY = self.y/self.gridSize
        if cells[int(indexX)][int(indexY)].green:
            return True
        