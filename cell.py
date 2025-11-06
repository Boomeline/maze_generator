
class Cell():
    def __init__(self, parent = None, x = 0 , y = 0):
        self.parent = parent 
        self.x = x
        self.y = y
        self.children = []
        self.visited = False
        self.done = False
        self.green = False 
        self.walls = {
            "t" : True,
            "b" : True,
            "l" : True,
            "r" : True}
        

 