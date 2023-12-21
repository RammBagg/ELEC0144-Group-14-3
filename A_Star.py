import heapq

def heuristic(node, goal):
    return abs(node - goal)

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
    neighbors = []

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == node:
                for ii in range(max(0, i-1), min(len(grid), i+2)):
                    for jj in range(max(0, j-1), min(len(grid[0]), j+2)):
                        if (ii, jj) != (i, j) and grid[ii][jj] not in obstacles:
                            neighbors.append(grid[ii][jj])

    return neighbors

def print_grid(grid, start, end, path, visited):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == start:
                print("S", end='\t')
            elif grid[i][j] == end:
                print("E", end='\t')
            elif grid[i][j] in path:
                print("*", end='\t')
            elif grid[i][j] in visited:
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
start_position = 16
end_position = 32

path, visited_nodes = astar(grid, start_position, end_position)

print_grid(grid, start_position, end_position, path, visited_nodes)
