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
        return self.player, self.window, self.maze


    def gen(self):
        draw = True
        gen = True
        fst = True
        while gen :
            try: 
                self.maze.neighbors()
                self.maze.gen()
            except IndexError:
                gen = False 


        if self.player.checkGreen(cells):
            sleep(1)
            draw = True 
            fst = False
            try: 
                self.maze.neighbors()
                self.maze.gen()
            except IndexError:
                gen = False 
            cells = self.maze.get()

    def draw(self):
        pass