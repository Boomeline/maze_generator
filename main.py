import pygame as pg
import random as rand 
from cell import Cell 
from mazegen import MazeGen
from time import sleep
from player import Player

grid_size = 40
cell_size = 15
width = grid_size * cell_size + 2  
height = grid_size * cell_size + 2
cells = [[None for y in range(grid_size)] for x in range(grid_size)]
for x in range(grid_size):
    for y in range(grid_size):
        cells[x][y] = Cell(None, x, y)



pg.init()

stack = []
window = pg.display.set_mode((width, height))
player = Player(cell_size, grid_size)
maze = MazeGen(stack, grid_size, cell_size, window, cells)
 

clock = pg.time.Clock()

def new():
    global cells 
    pg.Surface.fill(window, (0,0,0)) 
    cells = gen()
    return cells 

    
def gen(): 
    global cells
    cont = True   
    while cont:
        cont = maze.gen()
        cells = maze.get()
    return cells

def draw():
    global cells 
    maze.draw()
    if not player.move(cells):
        return False
    player.drawPlayer(window)
    if player.checkGreen(cells):
        cells = new()
    return True, cells

cells = gen() 
run = True
 
while run:

    #clock.tick(30)
    
    pg.Surface.fill(window, (0,0,0))
    run, cells = draw()  
    pg.display.flip()        

pg.quit()

 