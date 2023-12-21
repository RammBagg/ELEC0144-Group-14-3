import heapq
import math

class Grid:
    def __init__(self, rows, cols, obstacles):
        self.rows = rows
        self.cols = cols
        self.obstacles = obstacles
        self.graph = [[i * cols + j + 1 for j in range(cols)] for i in range(rows)]

    def is_valid(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols

    def is_obstacle(self, x, y):
        return self.graph[x][y] in self.obstacles

class AStar:
    def __init__(self, grid):
        self.grid = grid
        self.ROOT2 = math.sqrt(2)

    def heuristic(self, a, b):
        x1, y1 = (a - 1) // self.grid.cols, (a - 1) % self.grid.cols
        x2, y2 = (b - 1) // self.grid.cols, (b - 1) % self.grid.cols
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
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)]:
                new_x, new_y = x + dx, y + dy
                if self.grid.is_valid(new_x, new_y):
                    weight = 1 if dx == 0 or dy == 0 else self.ROOT2
                    neighbour = self.grid.graph[new_x][new_y]
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
