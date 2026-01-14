import pygame as pg
import random as rand 
from cell import Cell 
from mazegen import MazeGen
from time import sleep
from player import Player

grid_size = 20
cell_size = 25
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
    global maze 
    cells = [[None for y in range(grid_size)] for x in range(grid_size)]
    for x in range(grid_size):
        for y in range(grid_size):
            cells[x][y] = Cell(None, x, y)
    maze = MazeGen(stack, grid_size, cell_size, window, cells)
    pg.Surface.fill(window, (0,0,0)) 
    cells = gen()
    return cells, maze 

    
def gen(): 
    global cells
    cont = True   
    while cont:
        cont = maze.gen()
    cells = maze.get()
    return cells

def draw():
    global cells 
    global maze
    maze.draw()
    if not player.move(cells):
        return cells, maze, False
    player.drawPlayer(window)
    if player.checkGreen(cells):
        cells, maze = new()
    return cells, maze, True

cells = gen() 
run = True
 
while run:
    clock.tick()
    
    # print(clock)
    pg.Surface.fill(window, (0,0,0))
    cells, maze, run = draw()  
    pg.display.flip()        

pg.quit()

 