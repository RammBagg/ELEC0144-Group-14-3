import heapq
import math
from grid import Grid

class AStar:
    def __init__(self, grid):
        self.grid = grid
        self.ROOT2 = math.sqrt(2)

    def get_pos(self,x):
        coords = [(x - 1) // self.grid.cols, (x - 1) % self.grid.cols]
        return coords
    
    def get_vertex(self, x, y):
        return self.grid[x][y]

    def heuristic(self, a, b): # here a and b represent the 2 point we are taking the heuristic between
        x1, y1 = self.get_pos(a)
        x2, y2 = self.get_pos(b)

        # this calculated the euclidian distance between 
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def astar(self, start, end):
        priority_queue = [(0 + self.heuristic(start, end), 0, start)]
        iterations = 0

        distances = {vertex: float('infinity') for vertex in range(1, self.grid.rows * self.grid.cols + 1)}
        distances[start] = 0

        visited = set()

        while priority_queue:
            current_total_cost, current_distance, current_vertex = heapq.heappop(priority_queue)
            x, y = (current_vertex - 1) // self.grid.cols, (current_vertex - 1) % self.grid.cols

            if current_vertex in visited or self.grid.is_obstacle(x, y):
                continue

            visited.add(current_vertex)

            front = []
            for dx, dy in grid.directions:
                new_x, new_y = x + dx, y + dy
                if self.grid.is_valid(new_x, new_y):
                    weight = 1 if dx == 0 or dy == 0 else self.ROOT2
                    neighbour = self.grid.grid[new_x][new_y]
                    if self.grid.is_obstacle(new_x, new_y):
                        continue
                    distance = current_distance + weight
                    total_cost = distance + self.heuristic(neighbour, end)

                    front.append([weight, neighbour, current_vertex])
                    if distance < distances[neighbour]:
                        distances[neighbour] = distance
                        heapq.heappush(priority_queue, (total_cost, distance, neighbour))

            self.write_to_files(iterations, visited, front)
            iterations += 1

        return distances[end]

    def write_to_files(self, iterations, visited, front):
        with open("astar_visited.txt", "a") as visited_file:
            visited_file.write(f"Iteration {iterations}: {str(visited)}\n")

        with open("astar_front.txt", "a") as front_file:
            front_file.write(f"Iteration {iterations}:\n{{\n")
            for s in front:
                front_file.write(f"{str(s)}\n")
            front_file.write("}\n\n")


# Example usage
rows = 6
cols = 6
obstacles = [2, 10, 11, 20, 21, 27, 33]

grid = Grid(rows, cols, obstacles)
start_vertex = 16
end_vertex = 32

astar_instance = AStar(grid)
result = astar_instance.astar(start_vertex, end_vertex)

print(f"Shortest distance from {start_vertex} to {end_vertex}: {result}")
