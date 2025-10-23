import pygame as pg
import random as rand 
from cell import Cell 
from mazegen import MazeGen
from time import sleep

pg.init()

# grid_size = number of cells per side; cell_size = pixels per cell
grid_size = 40
cell_size = 15
width = grid_size * cell_size + 2  # small padding for border lines
height = grid_size * cell_size + 2
window = pg.display.set_mode((width, height))
grid = []
stack = [] 


run = True
draw = True
maze = MazeGen(stack, grid_size, cell_size, window)
# pg.display.flip()

while run:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False 
        if event.type == pg.KEYDOWN:    
            if event.key == pg.K_ESCAPE:
                run = False

    while draw:
        maze.neighbors()
        try:
            maze.gen()
        except IndexError:
            maze.draw()
            pg.display.flip()
            draw = False
pg.quit()

 