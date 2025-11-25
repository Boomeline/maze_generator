import pygame as pg
import random as rand 
from cell import Cell 
from mazegen import MazeGen
from time import sleep
from player import Player
from loop import Loop

grid_size = 40
cell_size = 15

pg.init()

loop = Loop(grid_size, cell_size)
player, window, maze = loop.call()

clock = pg.time.Clock()

loop.gen()
run = True
 
while run:

    #clock.tick(30)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False 
        if event.type == pg.KEYDOWN:    
            if event.key == pg.K_ESCAPE:
                run = False
    
    pg.Surface.fill(window, (0,0,0))
    loop.draw()  
    pg.display.flip()        

pg.quit()

 