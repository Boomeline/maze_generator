from cell import Cell
from random import choice,randint
import pygame as pg 

class MazeGen():

    def __init__(self, stack: list, scale: int, window ):
        self.window = window
        self.scale = scale
        self.stack = stack
        self.cells = [[None for y in range(scale)] for x in range(scale)]
        for x in range(scale):
            for y in range(20):
                self.cells[x][y] = Cell(None, x, y)
        self.current = self.cells[0][0]
        stack.append(self.current)
        self.current.visited = True
        self.coordinates = []
        self.validNeighbors = []
        # print(self.cells)
 

    def neighbors(self):

        # for x in range(20):
        #     for y in range(20):
        #         if (self.cells[x][y].x == self.current.x -1) or (self.cells[x][y].x == self.current.x +1):
        #             if (self.cells[x][y].y == self.current.y-1) or (self.cells[x][y].y == self.current.y +1):
        #                 validNeighbors.append(self.cells[x][y])
        #                 coordinates.append(x)
        #                 coordinates.append(y)
        # return validNeighbors

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
        cx, cy = self.current.x, self.current.y

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < 20 and 0 <= ny < 20:
                neighbor = self.cells[nx][ny]

                if not neighbor.visited:
                    self.validNeighbors.append(neighbor)
                    self.coordinates.append((nx, ny))
  

    def gen(self, maze):
        # neighbors() returns immediate neighbors at offsets of 1 cell
        # so wall-removal should use offsets of 1, not 2
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        while not self.validNeighbors:
            stacked = self.stack.pop()
            self.current = stacked
            self.validNeihgbors = maze.neighbors()
            # print("pop")
        
        else:
            side = randint(0, len(self.validNeighbors) - 1)   
            next = self.validNeighbors[side]
            # print(f"Gen: current=({self.current.x},{self.current.y}) next=({next.x},{next.y})")
            next.visited = True
            next.parent = self.current
            self.current.children.append(next)
            for dx, dy in dirs:
                if self.current.x + dx == next.x and self.current.y + dy == next.y:
                    # Determine which walls to remove based on dx/dy
                    if dx == 1:   # right
                        # print(' removing right wall of current and left of next')
                        self.current.walls["r"] = False
                        next.walls["l"] = False
                    elif dx == -1:  # left
                        # print(' removing left wall of current and right of next')
                        self.current.walls["l"] = False
                        next.walls["r"] = False
                    elif dy == 1:   # down
                        # print(' removing bottom wall of current and top of next')
                        self.current.walls["b"] = False
                        next.walls["t"] = False
                    elif dy == -1:  # up
                        # print(' removing top wall of current and bottom of next')
                        self.current.walls["t"] = False
                        next.walls["b"] = False
            self.current = next
            self.stack.append(next)




    # def gen(self):
    # stack = [self.current]   # start from current
    # while stack:
    #     current = stack[-1]
    #     self.current = current
    #     neis = self.neighbors()   # should return list of unvisited neighbors

    #     if neis:                  # if there are unvisited neighbors
    #         nxt = choice(neis)    # pick one at random
    #         nxt.visited = True
    #         nxt.parent = current
    #         current.children.append(nxt)
    #         stack.append(nxt)     # move into the neighbor
    #     else:
    #         stack.pop()           # backtrack
    #         if stack:
    #             self.current = stack[-1]

    def draw(self):
        color = 250, 250, 250
        # iterate using x (column) and y (row) so indexing matches how
        # self.cells is populated (self.cells[x][y])
        for x in range(len(self.cells)):
            for y in range(len(self.cells[x])):
                rect = pg.Rect(x*20, y*20, 20, 20)
                pg.draw.rect(self.window, color, rect)

                cell_obj = self.cells[x][y]

                # draw walls only when the corresponding flag is True
                if cell_obj.walls["t"]:  # top
                    pg.draw.line(self.window, (0, 0, 0), (x*20, y*20), (x*20 + 20, y*20), 2)
                if cell_obj.walls["b"]:  # bottom
                    pg.draw.line(self.window, (0, 0, 0), (x*20, y*20 + 20), (x*20 + 20, y*20 + 20), 2)
                if cell_obj.walls["l"]:  # left
                    pg.draw.line(self.window, (0, 0, 0), (x*20, y*20), (x*20, y*20 + 20), 2)
                if cell_obj.walls["r"]:  # right
                    pg.draw.line(self.window, (0, 0, 0), (x*20 + 20, y*20), (x*20 + 20, y*20 + 20), 2)