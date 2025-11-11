import pygame as pg
import random as rand 
from cell import Cell 
from mazegen import MazeGen
from time import sleep
from player import Player
from loop import Loop

grid_size = 20
cell_size = 30

pg.init()

player, window, maze = Loop()

clock = pg.time.Clock()

run = True

while run:

    clock.tick(30)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False 
        if event.type == pg.KEYDOWN:    
            if event.key == pg.K_ESCAPE:
                run = False

    player.move()
    player.drawPlayer(window)
    
    pg.display.flip()
    pg.Surface.fill(window, (0,0,0))        

pg.quit()

 