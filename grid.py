class Grid:
    '''
    Class which creates a representation for the grid.
    
    '''
    def __init__(self, rows: int, cols: int, obstacles: [int], directions:str="8-way") -> None:
        '''
        Initialises a grid.
        Each cell in the grid is assigned a value starting from 1 to V, where V = total number
        of vertices.

        :param rows: An integer value for the number of rows the grid must have.
        :param cols: An integer value for the number of columns the grid must have.
        :param obstacles: A list of integers, where each value is under the total number of cells the 
                          grid has, which represents where the obstacles are.
        :param directions: A string value equal to either '4-way' or '8-way' depending on the robots
                           constraints. Set to '8-way' by default.
        '''
        self.rows = rows
        self.cols = cols
        self.obstacles = obstacles
        self.V = self.rows * self.cols
        self.layout = [[i * cols + j + 1 for j in range(cols)] for i in range(rows)]
        if directions == "8-way":
            self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)]
        elif directions == "4-way":
            self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        else:
            raise ValueError("Enter a valid value for directions: '8-way' or '4-way'.")

    def is_valid(self, x: int, y: int) -> bool:
        '''
        Check if the coordinates are within the bounds of the grid.
        
        :param x: the x-coordinate.
        :param y: the y-coordinate

        :returns: True if the x-coordinate and y-coordinate are a valid position
                  on the grid.  
        '''
        return 0 <= x < self.rows and 0 <= y < self.cols

    def is_obstacle(self, *arg):
        '''
        Check if the cell specified is an obstacle by checking if its in
        the list of obstacles. 
        
        '''
        if len(arg) > 1:
            x, y = arg
            return self.layout[x][y] in self.obstacles
        else:
            x= arg[0]
            return x in self.obstacles
    
    def get_pos(self, x: int) -> [int]:
        '''
        Given a value of a cell, find the position/coordinates of the cell.

        :param x: An integer value which represents the number of the cell 
                  in the grid, from when the grid was initialised. 

        :returns: A list with the first value being the x-coordinate, and
                  the second value being the y-coordinate.
        '''
        coords = [(x - 1) // self.rows, (x - 1) % self.cols]
        return coords
    
    def get_vertex(self, x: int, y: int) -> int:
        '''
        Given the (x, y) coordinates, find which value represents the cells.

        :param x: Integer value for the x-coordinate.
        :param y: Integer value for the y-coordinate.

        :returns: The integer value stored in the cell.
        '''
        return self.layout[x][y]
    
