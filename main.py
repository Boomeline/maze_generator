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
            maze.draw(window , n)
            pg.display.flip()
            draw = False
pg.quit()

 