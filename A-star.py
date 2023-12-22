import heapq
import math
from grid import Grid

class AStar:
    def __init__(self, grid):
        """
        Initialize the AStar object with the given grid.

        Parameters:
        - grid (Grid): The grid on which the A* algorithm will be applied.
        """
        self.grid = grid
        self.front = []  # Current frontiers during the A* algorithm
        self.visited = set()  # Set of visited vertices
        self.front_file = open("astar_front.txt", "a")  # File to log frontiers
        self.visited_file = open("astar_visited.txt", "a")  # File to log visited vertices

    def get_pos(self, x):
        """
        Convert vertex number to grid coordinates.

        Parameters:
        - x (int): Vertex number.

        Returns:
        - tuple: (row, col) coordinates in the grid.
        """
        coords = [(x - 1) // self.grid.cols, (x - 1) % self.grid.cols]
        return coords
    
    def get_vertex(self, x, y):
        """
        Get the vertex number for the given grid coordinates.

        Parameters:
        - x (int): Row coordinate.
        - y (int): Column coordinate.

        Returns:
        - int: Vertex number.
        """
        return self.grid[x][y]

    def heuristic(self, a, b):
        """
        Calculate the heuristic (Euclidean distance) between two vertices.

        Parameters:
        - a (int): Vertex number for point A.
        - b (int): Vertex number for point B.

        Returns:
        - float: Euclidean distance between A and B.
        """
        x1, y1 = self.get_pos(a)
        x2, y2 = self.get_pos(b)
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def astar(self, start, end):
        """
        Run the A* algorithm to find the shortest path from start to end.

        Parameters:
        - start (int): Vertex number for the starting point.
        - end (int): Vertex number for the destination point.

        Returns:
        - float: Shortest distance from start to end.
        """
        priority_queue = [(0 + self.heuristic(start, end), 0, start)]
        iterations = 0

        distances = {vertex: float('infinity') for vertex in range(1, self.grid.rows * self.grid.cols + 1)}
        distances[start] = 0

        while priority_queue:
            # Extract the vertex with the lowest total cost from the priority queue
            current_total_cost, current_distance, current_vertex = heapq.heappop(priority_queue)
            x, y = (current_vertex - 1) // self.grid.cols, (current_vertex - 1) % self.grid.cols

            # Skip visited vertices and obstacles
            if current_vertex in self.visited or self.grid.is_obstacle(x, y):
                continue

            # Mark the current vertex as visited
            self.visited.add(current_vertex)

            front = []  # Temporary list to store the neighbors of the current vertex
            for dx, dy in self.grid.directions:
                new_x, new_y = x + dx, y + dy
                if self.grid.is_valid(new_x, new_y):
                    weight = 1 if dx == 0 or dy == 0 else math.sqrt(2)  # Calculate the movement cost
                    neighbour = self.grid.layout[new_x][new_y]
                    if self.grid.is_obstacle(new_x, new_y):
                        continue
                    distance = current_distance + weight
                    total_cost = distance + self.heuristic(neighbour, end)

                    # Add the neighbor to the temporary front list
                    front.append([weight, neighbour, current_vertex])

                    # Update the distance and total cost if a shorter path is found
                    if distance < distances[neighbour]:
                        distances[neighbour] = distance
                        heapq.heappush(priority_queue, (total_cost, distance, neighbour))

            # Log the current state to files
            self.write_to_files(iterations, self.visited, front)
            iterations += 1

        # Close the log files
        self.visited_file.close()
        self.front_file.close()

        return distances[end]

    def write_to_files(self, iterations, visited, front):
        """
        Write information about visited vertices and current frontiers to files.

        Parameters:
        - iterations (int): Current iteration number.
        - visited (set): Set of visited vertices.
        - front (list): List of current frontiers.
        """
        with open("astar_visited.txt", "a") as visited_file:
            visited_file.write(f"Iteration {iterations}: {str(visited)}\n")

        with open("astar_front.txt", "a") as front_file:
            front_file.write(f"Iteration {iterations}:\n{{\n")
            for s in front:
                front_file.write(f"{str(s)}\n")
            front_file.write("}\n\n")

rows = 6
cols = 6
obstacles = [2, 10, 11, 20, 21, 27, 33]

grid = Grid(rows, cols, obstacles)
start_vertex = 16
end_vertex = 32

astar_instance = AStar(grid)
result = astar_instance.astar(start_vertex, end_vertex)

print(f"Shortest distance from {start_vertex} to {end_vertex}: {result}")
