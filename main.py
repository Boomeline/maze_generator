import pygame as pg
import random as rand 
from cell import Cell 
from mazegen import MazeGen
from time import sleep
from player import Player
from loop import Loop

grid_size = 40
cell_size = 15
width = grid_size * cell_size + 2  
height = grid_size * cell_size + 2

pg.init()

loop = Loop(grid_size, cell_size)
player, window, maze = loop.call()
stack = []
window = pg.display.set_mode((width, height))
cells = maze.get()

player = Player(cell_size, grid_size)
maze = MazeGen(stack, grid_size, cell_size, window)

clock = pg.time.Clock()
    
def gen(self):    
    while True:
        cont = maze.gen()
        if not cont:
            break

def draw(self):
    maze.draw()
    if player.move(cells) == False:
        return False
    player.drawPlayer(window)
    if player.checkGreen(cells):
        sleep(1) 
        for _ in range(width, height): 
            maze.neighbors()
            maze.gen()
            cells = self.maze.get()
    return True

run = True
 
while run:

    #clock.tick(30)
    
    pg.Surface.fill(window, (0,0,0))
    run = loop.draw()  
    pg.display.flip()        

pg.quit()

 