from cell import Cell
from random import choice,randint
import pygame as pg 

class MazeGen():

    def __init__(self, stack: list):
        self.cells = [[None for y in range(20)] for x in range(20)]
        for x in range(20):
            for y in range(20): 
                self.cells[x][y] = Cell()
        self.current = self.cells[0][0]
        stack.append(self.current)
        self.cells[0][0] = self.current
        self.current.visited = True
        self.coordinates = []
        # print(self.cells)
 
    
    def drawGrid(self,  height = 400, scale = 20, width = 400):
        for x in range(20):
            for y in range(20):
                cell =  Cell(None, x, y)
                self.cells[x][y] = cell


    def neighbors(self):
        validNeighbors = []

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
                    validNeighbors.append(neighbor)
                    self.coordinates.append((nx, ny))
        
        return validNeighbors
  

    def gen(self, neigbors:list , maze, stack):
        dirs = [(0, -2), (0, 2), (-2, 0), (2, 0)]
        while not neigbors:
            stacked = stack.pop()
            self.current = stacked
            neigbors = maze.neighbors()
            print("pop")
        
        else:
            side = randint(0, len(neigbors) - 1)   
            next = neigbors[side]
            next.visited = True
            next.parent = self.current
            self.current.children.append(next)
            for dx, dy in dirs:
                if self.current.x + dx == next.x and self.current.y + dy == next.y:
                    if dx == 2:   # right
                        self.current.walls["r"] = False
                        next.walls["l"] = False
                    elif dx == -2:  # left
                        self.current.walls["l"] = False
                        next.walls["r"] = False
                    elif dy == 2:   # down
                        self.current.walls["b"] = False
                        next.walls["t"] = False
                    elif dy == -2:  # up
                        self.current.walls["t"] = False
                        next.walls["b"] = False
            self.current = next
            stack.append(next)
            print(stack)



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

    def draw(self, window, neigbors):
        color = 250, 250, 250
        dirs = [(0, -2), (0, 2), (-2, 0), (2, 0)]
        for row in range(len(self.cells)):
            for cell in range(len(self.cells[row])):
                rect = pg.Rect(cell*20 ,row*20  , 20, 20)
                pg.draw.rect(window , color , rect)
                for dx, dy in dirs:
                    if self.cells[cell][row].walls["t"] and dy == -2:  # top
                        pg.draw.line(window, (0, 0, 0), (cell*20, row*20), (cell*20 + 20, row*20), 2)
                    if self.cells[cell][row].walls["b"] and dy == 2:   # bottom
                        pg.draw.line(window, (0, 0, 0), (cell*20, row*20 + 20), (cell*20 + 20, row*20 + 20), 2)
                    if self.cells[cell][row].walls["l"] and dx == -2:  # left
                        pg.draw.line(window, (0, 0, 0), (cell*20, row*20), (cell*20, row*20 + 20), 2)
                    if self.cells[cell][row].walls["r"] and dx == 2:   # right
                        pg.draw.line(window, (0, 0, 0), (cell*20 + 20, row*20), (cell*20 + 20, row*20 + 20), 2)