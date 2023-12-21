import math

class Grid:
    
    def __init__(self, rows, cols, obstacles):
        self.rows = rows
        self.cols = cols
        
        self.obstacles = obstacles
        self.layout = [[i * cols + j + 1 for j in range(cols)] for i in range(rows)]
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)]

    def is_valid(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols

    def is_obstacle(self, *arg):
        if len(arg) > 1:
            x, y = arg
            return self.layout[x][y] in self.obstacles
        else:
            x= arg[0]
            return x in self.obstacles
    
    def get_pos(self, x):
        coords = [(x - 1) // self.rows, (x - 1) % self.cols]
        return coords
    
    def get_vertex(self, x, y):
        return self.layout[x][y]
    
