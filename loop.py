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
        print("gen")
        for _ in range(self.width, self.height): 
                self.maze.neighbors()
                self.maze.gen()

        if self.player.checkGreen(self.cells):
            sleep(1) 
            for _ in range(self.width, self.height): 
                self.maze.neighbors()
                self.maze.gen()
                self.cells = self.maze.get()

    def draw(self):
        pass