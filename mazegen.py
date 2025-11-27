from cell import Cell
from random import randint
import pygame as pg 

class MazeGen():

    def __init__(self, stack: list, grid_size: int, cell_size: int, window ):
        self.window = window
        self.grid_size = grid_size
        self.cell_size = cell_size
        self.stack = stack
        self.cells = [[None for y in range(grid_size)] for x in range(grid_size)]
        for x in range(grid_size):
            for y in range(grid_size):
                self.cells[x][y] = Cell(None, x, y)
        self.current = self.cells[0][0]
        stack.append(self.current)
        self.current.visited = True
        self.coordinates = []
        self.validNeighbors = []
        # print(self.cells)

    def get(self):
        return self.cells
 

    def neighbors(self):
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        self.validNeighbors = []
        cx, cy = self.current.x, self.current.y
        for dx, dy in dirs:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < self.grid_size and 0 <= ny < self.grid_size:
                neighbour = self.cells[nx][ny]
                if not neighbour.visited:
                    self.validNeighbors.append(neighbour)
        return self.validNeighbors
  

    def gen(self):
        # Perform a single DFS step: carve to a random unvisited neighbor
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        self.neighbors()
        if self.validNeighbors:
            side = randint(0, len(self.validNeighbors) - 1)
            nxt = self.validNeighbors[side]
            # push current to stack (path)
            self.stack.append(self.current)
            # remove walls between current and nxt
            if self.current.x + 1 == nxt.x and self.current.y == nxt.y:  # right
                self.current.walls["r"] = False
                nxt.walls["l"] = False
            elif self.current.x - 1 == nxt.x and self.current.y == nxt.y:  # left
                self.current.walls["l"] = False
                nxt.walls["r"] = False
            elif self.current.y + 1 == nxt.y and self.current.x == nxt.x:  # down
                self.current.walls["b"] = False
                nxt.walls["t"] = False
            elif self.current.y - 1 == nxt.y and self.current.x == nxt.x:  # up
                self.current.walls["t"] = False
                nxt.walls["b"] = False

            # move to next cell and mark visited
            self.current = nxt
            self.current.visited = True
            return True

        # No unvisited neighbors: backtrack if possible
        if self.stack:
            self.current = self.stack.pop()
            return True

        # Stack empty and no neighbors -> generation complete
        return False

    def draw(self):
        pg.Surface.fill(self.window, (250,250,250))
        for y in range(len(self.cells)):
            for x in range(len(self.cells[y])):
                cell_obj = self.cells[x][y]

                if cell_obj.walls["t"]:  # top
                    pg.draw.line(self.window, (0, 0, 0), (x * self.cell_size, y * self.cell_size), (x * self.cell_size + self.cell_size, y * self.cell_size), 2)
                if cell_obj.walls["b"]:  # bottom
                    pg.draw.line(self.window, (0, 0, 0), (x * self.cell_size, y * self.cell_size + self.cell_size), (x * self.cell_size + self.cell_size, y * self.cell_size + self.cell_size), 2)
                if cell_obj.walls["l"]:  # left
                    pg.draw.line(self.window, (0, 0, 0), (x * self.cell_size, y * self.cell_size), (x * self.cell_size, y * self.cell_size + self.cell_size), 2)
                if cell_obj.walls["r"]:  # right
                    pg.draw.line(self.window, (0, 0, 0), (x * self.cell_size + self.cell_size, y * self.cell_size), (x * self.cell_size + self.cell_size, y * self.cell_size + self.cell_size), 2)


    def animate(self, x = 0 , y = 0):
        color = 250, 250, 250

        if randint(0, 800) == 1:
            color = (100, 250, 100)
            self.cells[x][y].green = True
        rect = pg.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
        pg.draw.rect(self.window, color, rect)

        cell_obj = self.cells[x][y]

        if cell_obj.walls["t"]:  # top
            pg.draw.line(self.window, (0, 0, 0), (x * self.cell_size, y * self.cell_size), (x * self.cell_size + self.cell_size, y * self.cell_size), 2)
        if cell_obj.walls["b"]:  # bottom
            pg.draw.line(self.window, (0, 0, 0), (x * self.cell_size, y * self.cell_size + self.cell_size), (x * self.cell_size + self.cell_size, y * self.cell_size + self.cell_size), 2)
        if cell_obj.walls["l"]:  # left
            pg.draw.line(self.window, (0, 0, 0), (x * self.cell_size, y * self.cell_size), (x * self.cell_size, y * self.cell_size + self.cell_size), 2)
        if cell_obj.walls["r"]:  # right
            pg.draw.line(self.window, (0, 0, 0), (x * self.cell_size + self.cell_size, y * self.cell_size), (x * self.cell_size + self.cell_size, y * self.cell_size + self.cell_size), 2)
        if y == self.grid_size  - 1:
            x += 1
            y = 0
        else: 
            y += 1
        return x, y