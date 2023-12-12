import heapq

def heuristic(node, goal):
    x1, y1 = node
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)

def astar(grid, start, end):
    priority_queue = [(0, start)]
    visited = set()
    came_from = {}

    iteration = 0

    while priority_queue:
        
        current_cost, current_node = heapq.heappop(priority_queue)

        if current_node == end:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            path.reverse()

            return path, visited

        visited.add(current_node)
        neighbors = get_neighbors(current_node, grid)
        
        for neighbor in neighbors:
            if neighbor not in visited:
                cost = current_cost + 1
                total_cost = cost + heuristic(neighbor, end)
                heapq.heappush(priority_queue, (total_cost, neighbor))
                came_from[neighbor] = current_node

        iteration += 1

    return None, visited

def get_neighbors(node, grid):
    x, y = node
    neighbors = []

    for i in range(max(0, x-1), min(6, x+2)):
        for j in range(max(0, y-1), min(6, y+2)):
            if (i, j) != node and grid[i][j] not in obstacles:
                neighbors.append((i, j))

    return neighbors

def print_grid(grid, start, end, path, visited):
    for i in range(6):
        for j in range(6):
            if (i, j) == start:
                print("S", end='\t')
            elif (i, j) == end:
                print("E", end='\t')
            elif (i, j) in path:
                print("*", end='\t')
            elif (i, j) in visited:
                print("V", end='\t')
            else:
                print(grid[i][j], end='\t')
        print()

# Initialize the grid with obstacles
grid = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, -1, 16, 17, 18],
    [19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36]
]

obstacles = [2, 10, 11, 20, 21, 27, 33]
start_position = (0, 0)
end_position = (5, 5)

path, visited_nodes = astar(grid, start_position, end_position)

print_grid(grid, start_position, end_position, path, visited_nodes)
