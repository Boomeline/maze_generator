import pygame as pg
import random as rand 
from cell import Cell 
from mazegen import MazeGen
from time import sleep
from player import Player

pg.init()

# grid_size = number of cells per side; cell_size = pixels per cell
grid_size = 20
cell_size = 30
width = grid_size * cell_size + 2  # small padding for border lines
height = grid_size * cell_size + 2
window = pg.display.set_mode((width, height))
stack = [] 
player = Player(cell_size, grid_size)

run = True
draw = True
maze = MazeGen(stack, grid_size, cell_size, window)
gen = True 
clock = pg.time.Clock()

while gen:
    try: 
        maze.neighbors()
        maze.gen()
    except IndexError:
        gen = False 
cells = maze.get()
fst = True
draw =True

while run:

    # clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False 
        if event.type == pg.KEYDOWN:    
            if event.key == pg.K_ESCAPE:
                run = False

    player.move()
    player.drawPlayer(window)

    if player.checkGreen(cells):
        sleep(1)
        draw = True 
        fst = False
        try: 
            maze.neighbors()
            maze.gen()
        except IndexError:
            gen = False 
        cells = maze.get()

    if draw:
        try: 
            if fst:
                x, y = maze.draw()
                fst = False
            else:
                x, y = maze.draw(x, y)
                pg.display.update()
        except IndexError:
            print("error")
            draw = False
             
        

pg.quit()

 