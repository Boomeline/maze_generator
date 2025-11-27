import pygame as pg

class Player ():
    def __init__(self, cellSize : int, grid_size ):
        self.cellSize = cellSize
        self.gridSize = grid_size
        self.x, self.y = 0, 0
        self.gx, self.gy = self.x // self.cellSize, self.x // self.cellSize


    def drawPlayer(self, screen):
        pg.draw.rect(screen, (255, 0, 0), (self.x + 3, self.y + 3, self.cellSize - 4, self.cellSize- 4 )) 
        pass

    def move(self, cells : list):
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        neighbors = []
        cx, cy = self.gx, self.gy
        for dx, dy in dirs:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < self.gridSize and 0 <= ny < self.gridSize:
                neighbour = cells[nx][ny]
                if not neighbour.visited:
                    neighbors.append(neighbour)
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                print(event.key)
                if event.key == pg.K_UP:
                    moved = self.check_walls(dirs[0],neighbors)
                    print(moved)
                    if moved:
                        self.y -= self.cellSize
                if event.key == pg.K_DOWN:
                    moved = self.check_walls(dirs[1],neighbors)
                    print(moved)
                    if moved:
                        self.y += self.cellSize
                if event.key == pg.K_LEFT:
                    moved = self.check_walls(dirs[2],neighbors)
                    print(moved)
                    if moved:
                        self.x -= self.cellSize
                if event.key == pg.K_RIGHT:
                    moved = self.check_walls(dirs[3],neighbors)
                    print(moved)
                    if moved:
                        self.x += self.cellSize 
                if event.type == pg.QUIT:
                    return  False 
                if event.type == pg.KEYDOWN:    
                    if event.key == pg.K_ESCAPE:
                        return  False 

    def check_walls(self, side : tuple, neighbors):
        print(side)
        print(self.x // self.cellSize, self.y // self.cellSize)
        if neighbors:
            for neighbor in neighbors:
                print(neighbor.x, neighbor.y)
                if neighbor.x - (self.x // self.cellSize) == side[0] and neighbor.y - (self.y // self.cellSize)  == side[1]:
                    return True 
        return False 

    def checkGreen(self, cells: list):
        indexX = self.x/self.gridSize
        indexY = self.y/self.gridSize
        if cells[int(indexX)][int(indexY)].green:
            return True
        