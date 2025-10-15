import pygame as pg
import random as rand 
from cell import Cell 
from mazegen import MazeGen
from time import sleep

pg.init()

width = 400
height = 400
scale = 20
window = pg.display.set_mode((width, height))
grid = []
stack = [] 


run = True
draw = True
maze = MazeGen(stack)
maze.drawGrid()
# pg.display.flip()

while run:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False 
        if event.type == pg.KEYDOWN:    
            if event.key == pg.K_ESCAPE:
                run = False

    while draw:
        n = maze.neighbors()
        print(stack)
        try:
            maze.gen(n, maze , stack)
        except IndexError:
            # generation finished (stack emptied) — print debug info
            # show sample walls and a total count of wall sides still True
            total_true = 0
            for x in range(20):
                for y in range(20):
                    total_true += sum(1 for v in maze.cells[x][y].walls.values() if v)

            print("Total wall sides still True:", total_true)
            print("Sample (0,0).walls:", maze.cells[0][0].walls)
            print("Sample (0,1).walls:", maze.cells[0][1].walls)
            print("Sample (1,0).walls:", maze.cells[1][0].walls)

            maze.draw(window , n)
            pg.display.flip()
            draw = False
pg.quit()

 