import heapq, math
from abc import abstractmethod

class Dijkstra:
    '''
    Dijkstra class.
    Implements the dijkstra algorithm on a n x m grid.
    Can accept a list of obstacles, which is a list of numbers of those nodes
    considered an obstacle in the paths.

    '''
    
    def __init__(self, rows, cols, obstacles) -> None:        
        self.clear_files()
        self.inf = float('inf')
        self.directions = [[0, 1], [1, 0], [0, -1], [-1, 0], [-1, -1], [-1, 1], [1, 1], [1, -1]]
        self.ROOT2 = math.sqrt(2)
        self.front_file = open("dijkstra_front.txt", "a")
        self.visited_file = open("dijkstra_visited.txt", "a")
        self.V = rows * cols
        self.rows = rows
        self.cols = cols
        self.grid = []
        self.front = []
        self.visited = set()
        # Dictionary to store distances from the start vertex
        self.distances = {vertex: float('infinity') for vertex in range(1, self.V + 1)}        
        self.obstacles = obstacles
        self.initialise_grid()

    @abstractmethod
    def clear_files(self):
        open("dijkstra_front.txt", "w").close()
        open("dijkstra_visited.txt", "w").close()

    def initialise_grid(self):
        v = 1
        for i in range(self.rows):
            self.grid.append([])
            for j in range(self.cols):
                self.grid[i].append(v)
                v += 1

    def update_files(self, iterations):
        self.visited_file.write(f"Iteration {iterations}: ")
        self.visited_file.write(str(self.visited) + "\n")

        self.front_file.write(f"Iteration {iterations}: \n")
        write_to_file = "{ \n"
        for s in self.front:
            write_to_file += str(s) + "\n"
        write_to_file += "} \n\n"

        self.front_file.write(write_to_file)
    
    def backpropagation(self, start, end):
        # Backpropagation to find the shortest path
        path = []
        current_vertex = end
        while current_vertex != start:
            path.insert(0, current_vertex)
            coords = [(current_vertex - 1) // self.rows, (current_vertex - 1) % self.cols]
            for d in self.directions:
                if coords[0] + d[0] < self.rows and coords[0] + d[0] >= 0 and coords[1] + d[1] < self.cols and coords[1] + d[1] >= 0:
                    v = self.grid[coords[0] + d[0]][coords[1] + d[1]]
                    if v in self.obstacles:
                        continue
                    if self.distances[v] < self.distances[current_vertex]:
                        current_vertex = v

        path.insert(0, start)
        return path

    def run(self, start, end):
        # Priority queue to store vertices and their distances
        priority_queue = [(0, start)]
        iterations = 0
        self.distances[start] = 0

        while priority_queue:
                # Get the vertex with the smallest distance
                current_distance, current_vertex = heapq.heappop(priority_queue)
                coords = [(current_vertex - 1) // self.rows, (current_vertex - 1) % self.cols]

                # Check if the current path is longer than the known distance
                if current_vertex in self.visited:
                    continue
                
                # Mark the current vertex as visited
                self.visited.add(current_vertex)
                
                # Update distances for neighboring vertices
                for d in self.directions:
                    if coords[0] + d[0] < self.rows and coords[0] + d[0] >= 0 and coords[1] + d[1] < self.cols and coords[1] + d[1] >= 0:
                        weight = 0
                        if d[0] == 0 or d[1] == 0:
                            weight = 1
                        else:
                            weight = self.ROOT2
                        neighbour = self.grid[coords[0] + d[0]][coords[1] + d[1]]
                        if neighbour in self.obstacles:
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

obstacles = [10, 11, 20, 21, 27]

d = Dijkstra(6, 6, obstacles=obstacles)

d.run(start_vertex, end_vertex)

