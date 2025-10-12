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
        for row in range(len(self.cells)):
            for cell in range(len(self.cells[row])):
                for neig in neigbors:
                    if not neig in self.cells[row][cell].children:
                        color = 0, 0, 0
                rect = pg.Rect(cell*20 ,row*20  , 20, 20)
                pg.draw.rect(window , color , rect)