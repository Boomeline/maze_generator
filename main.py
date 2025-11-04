import pygame as pg
import random as rand 
from cell import Cell 
from mazegen import MazeGen
from time import sleep
from player import Player

pg.init()

# grid_size = number of cells per side; cell_size = pixels per cell
grid_size = 40
cell_size = 15
width = grid_size * cell_size + 2  # small padding for border lines
height = grid_size * cell_size + 2
window = pg.display.set_mode((width, height))
grid = []
stack = [] 
player = Player(cell_size)

run = True
draw = True
maze = MazeGen(stack, grid_size, cell_size, window)
# pg.display.flip()
gen = True 
while gen:
    try: 
        maze.neighbors()
        maze.gen()
    except IndexError:
        gen = False 

fst = True
draw =True

while run:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False 
        if event.type == pg.KEYDOWN:    
            if event.key == pg.K_ESCAPE:
                run = False

    # player.move()
    # player.draw()

        try: 
            if fst:
                x, y = maze.draw()
                fst = False
            else:
                x, y = maze.draw(x, y)
                pg.display.update()
        except IndexError:
            draw = False
        

pg.quit()

 