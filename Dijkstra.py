import heapq, math
from abc import abstractmethod
from grid import Grid

class Dijkstra:
    '''
    Dijkstra class.
    Implements the dijkstra algorithm on a n x m grid.
    Can accept a list of obstacles, which is a list of numbers of those nodes
    considered an obstacle in the paths.

    '''
    
    def __init__(self, grid: 'Grid') -> None:      
        '''
        Initialise variables for the Dikjstra algorithm. Requires a grid to perform
        the algorithm on.

        :param grid: of type 'Grid'.
        
        '''  
        self.clear_files()
        self.front_file = open("dijkstra_front.txt", "a")
        self.visited_file = open("dijkstra_visited.txt", "a")
        self.grid = grid
        self.front = []
        self.visited = set()
        self.ROOT2 = math.sqrt(2)
        # Dictionary to store distances from the start vertex
        self.distances = {vertex: float('infinity') for vertex in range(1, self.grid.V + 1)}        

    @abstractmethod
    def clear_files(self) -> None:
        '''
        Clear the text files before running the algorithm again. 
        This is to ensure previous data of previous runs does not conflict with any new
        data written to the files. 
        '''
        open("dijkstra_front.txt", "w").close()
        open("dijkstra_visited.txt", "w").close()

    def update_files(self, iterations: int) -> None:
        '''
        Write the current progress of the dikjstra algorithm, including the visited 
        list which contains vertices which have been explored, and the front list which 
        is the vertices currently being considered at a particular iteration of the algorithm.

        :param iterations: An integer value indicating progress of the algorithm by the number
        of the loops that have occurred so far.

        '''
        self.visited_file.write(f"Iteration {iterations}: ")
        self.visited_file.write(str(self.visited) + "\n")

        self.front_file.write(f"Iteration {iterations}: \n")
        write_to_file = "{ \n"
        for s in self.front:
            write_to_file += str(s) + "\n"
        write_to_file += "} \n\n"

        self.front_file.write(write_to_file)
    
    def backpropagation(self, start: int, end: int) -> [int]:
        '''
        Backpropagation to find the shortest path after dikjstra algorithm has finished finding
        the matrix of minimum distances from the starting vertex to all other vertices of the 
        graph.

        :param start: An integer value representing which cell is the path should start from.
        :param end: An integer value representing the cell the path should end at.

        :returns: The path is returned a list of integers, where each integer represents the cells
                  the robot must travel through to reach its destination.
        '''
        # Backpropagation to find the shortest path
        path = []
        current_vertex = end
        while current_vertex != start:
            path.insert(0, current_vertex)
            coords = grid.get_pos(current_vertex)
            for delta_x, delta_y in self.grid.directions:
                if self.grid.is_valid(coords[0] + delta_x, coords[1] + delta_y):
                    v = self.grid.get_vertex(coords[0] + delta_x, coords[1] + delta_y)
                    if self.grid.is_obstacle(v):
                        continue
                    if self.distances[v] < self.distances[current_vertex]:
                        current_vertex = v

        path.insert(0, start)
        return path

    def run(self, start: int, end: int) -> None:
        # Priority queue to store vertices and their distances
        priority_queue = [(0, start)]
        iterations = 0
        self.distances[start] = 0

        while priority_queue:
                # Get the vertex with the smallest distance
                current_distance, current_vertex = heapq.heappop(priority_queue)
                coords = grid.get_pos(current_vertex)

                # Check if the current path is longer than the known distance
                if current_vertex in self.visited:
                    continue
                
                # Mark the current vertex as visited
                self.visited.add(current_vertex)
                
                # Update distances for neighboring vertices
                for delta_x, delta_y in self.grid.directions:
                    if self.grid.is_valid(coords[0] + delta_x, coords[1] + delta_y):
                        weight = 1 if delta_x == 0 or delta_y == 0 else math.sqrt(2)
                        neighbour = self.grid.get_vertex(coords[0] + delta_x, coords[1] + delta_y)
                        if self.grid.is_obstacle(neighbour):
                            continue
                        distance = current_distance + weight
                        
                        self.front.append([weight, neighbour, current_vertex])
                        # If a shorter path is found, update the distance
                        if distance < self.distances[neighbour]:
                            self.distances[neighbour] = distance
                            heapq.heappush(priority_queue, (distance, neighbour))
                
                
                self.update_files(iterations)
                iterations += 1

        self.visited_file.close()
        self.front_file.close()

        path = self.backpropagation(start, end)


        print(f"Shortest distance from {start_vertex} to {end_vertex}: {self.distances[end]} \nWith the path: {path}")
    


start_vertex = 5
end_vertex = 32  # Specify the ending vertex

obstacles = [10, 11, 20, 21, 27, 33]

grid = Grid(6, 6, obstacles)

d = Dijkstra(grid)

d.run(start_vertex, end_vertex)

