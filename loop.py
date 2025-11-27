import pygame as pg
import random as rand 
from cell import Cell 
from mazegen import MazeGen
from time import sleep
from player import Player

class Loop():
    def __init__(self, grid_size, cell_size):
        self.width = grid_size * cell_size + 2  
        self.height = grid_size * cell_size + 2
        self.stack = []
        self.window = pg.display.set_mode((self.width, self.height))
        self.player = Player(cell_size, grid_size)
        self.maze = MazeGen(self.stack, grid_size, cell_size, self.window)
        self.cells = self.maze.get()

    def call(self):
        return self.player, self.window, self.maze

    def gen(self):
        while True:
            cont = self.maze.gen()
            if not cont:
                break

    
    def draw(self):
        self.maze.draw()
        px = self.player.x // self.player.cellSize
        py = self.player.y // self.player.cellSize
        maze_nei = self.maze.neighbors()
        player_neighbors = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = px + dx, py + dy
            if 0 <= nx < self.maze.grid_size and 0 <= ny < self.maze.grid_size:
                player_neighbors.append(self.maze.cells[nx][ny])
        print(f"{self.player.x},{self.player.y}")
        print(f"{px},{py}")
        print(f"{[(n.x,n.y) for n in maze_nei]}")
        print(f"{[(n.x,n.y) for n in player_neighbors]}")
        if self.player.move(player_neighbors) == False:
            return False
        self.player.drawPlayer(self.window)
        if self.player.checkGreen(self.cells):
            sleep(1) 
            for _ in range(self.width, self.height): 
                self.maze.neighbors()
                self.maze.gen()
                self.cells = self.maze.get()
        return True