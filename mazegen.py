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
            for y in range(scale):
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

        # reset the neighbor lists each time so we don't accumulate stale entries
        self.validNeighbors = []
        self.coordinates = []

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        cx, cy = self.current.x, self.current.y

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < self.scale and 0 <= ny < self.scale:
                neighbor = self.cells[nx][ny]

                if not neighbor.visited:
                    self.validNeighbors.append(neighbor)
                    self.coordinates.append((nx, ny))
  

    def gen(self):
        # neighbors() returns immediate neighbors at offsets of 1 cell
        # so wall-removal should use offsets of 1, not 2
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        # If there are no valid neighbors, pop/backtrack until we find one
        while not self.validNeighbors:
            stacked = self.stack.pop()
            self.current = stacked
            # repopulate valid neighbors for the new current
            self.neighbors()
            # if stack becomes empty, stack.pop() will raise IndexError and the caller
            # (main.py) handles it to finish generation.

        # choose a random neighbor and carve a path
        side = randint(0, len(self.validNeighbors) - 1)
        next = self.validNeighbors[side]
        next.visited = True
        next.parent = self.current
        self.current.children.append(next)
        for dx, dy in dirs:
            if self.current.x + dx == next.x and self.current.y + dy == next.y:
                # Determine which walls to remove based on dx/dy
                if dx == 1:   # right
                    self.current.walls["r"] = False
                    next.walls["l"] = False
                elif dx == -1:  # left
                    self.current.walls["l"] = False
                    next.walls["r"] = False
                elif dy == 1:   # down
                    self.current.walls["b"] = False
                    next.walls["t"] = False
                elif dy == -1:  # up
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
                rect = pg.Rect(x * self.scale, y * self.scale, self.scale, self.scale)
                pg.draw.rect(self.window, color, rect)

                cell_obj = self.cells[x][y]

                # draw walls only when the corresponding flag is True
                if cell_obj.walls["t"]:  # top
                    pg.draw.line(self.window, (0, 0, 0), (x * self.scale, y * self.scale), (x * self.scale + self.scale, y * self.scale), 2)
                if cell_obj.walls["b"]:  # bottom
                    pg.draw.line(self.window, (0, 0, 0), (x * self.scale, y * self.scale + self.scale), (x * self.scale + self.scale, y * self.scale + self.scale), 2)
                if cell_obj.walls["l"]:  # left
                    pg.draw.line(self.window, (0, 0, 0), (x * self.scale, y * self.scale), (x * self.scale, y * self.scale + self.scale), 2)
                if cell_obj.walls["r"]:  # right
                    pg.draw.line(self.window, (0, 0, 0), (x * self.scale + self.scale, y * self.scale), (x * self.scale + self.scale, y * self.scale + self.scale), 2)