import pygame as pg

class Player ():
    def __init__(self, cellSize : int, grid_size ):
        self.cellSize = cellSize
        self.gridSize = grid_size
        self.x, self.y = 0, 0
        self.gx, self.gy = self.x // self.cellSize, self.y // self.cellSize


    def drawPlayer(self, screen):
        pg.draw.rect(screen, (255, 0, 0), (self.x + 3, self.y + 3, self.cellSize - 4, self.cellSize- 4 )) 
        pass


    def neigh_pl(self, cells : list):
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        neighbors = []
        for dx, dy in dirs:
            nx, ny = self.gx + dx, self.gy + dy
            if 0 <= nx < self.gridSize and 0 <= ny < self.gridSize:
                neighbour = cells[nx][ny]
                # print(neighbour)
                neighbors.append(neighbour)
        return neighbors

    def move(self, cells : list):
        self.gx = self.x // self.cellSize
        self.gy =  self.y // self.cellSize
        neighbors = self.neigh_pl(cells)
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for event in pg.event.get():
            if event.type == pg.QUIT:
                    return False 
            if event.type == pg.KEYDOWN:    
                if event.key == pg.K_ESCAPE:
                    return False 
                # print(event.key)
                if event.key == pg.K_w or event.key == pg.K_UP:
                    moved = self.check_walls(dirs[0], cells)
                    print(moved)
                    if moved:
                        self.y -= self.cellSize
                if event.key == pg.K_s or event.key == pg.K_DOWN:
                    moved = self.check_walls(dirs[1], cells)
                    print(moved)
                    if moved:
                        self.y += self.cellSize
                if event.key == pg.K_a  or event.key == pg.K_LEFT:
                    moved = self.check_walls(dirs[2], cells)
                    print(moved)
                    if moved:
                        self.x -= self.cellSize
                if event.key == pg.K_d  or event.key == pg.K_RIGHT:
                    moved = self.check_walls(dirs[3], cells)
                    print(moved)
                    if moved:
                        self.x += self.cellSize 
        return True 

    def check_walls(self, side: tuple, cells):
        print(side)
        cx, cy = self.gx, self.gy
        # sanity check indices
        if not (0 <= cx < self.gridSize and 0 <= cy < self.gridSize):
            return False

        current = cells[cx][cy]
        # up
        if side == (0, -1):
            return not current.walls.get("t", True)
        # down
        if side == (0, 1):
            return not current.walls.get("b", True)
        # left
        if side == (-1, 0):
            return not current.walls.get("l", True)
        # right
        if side == (1, 0):
            return not current.walls.get("r", True)

        return False

    def checkGreen(self, cells: list):
        if cells[self.gx][self.gy].green:
            return True
        