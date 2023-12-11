import math
import heapq
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

class Node:
    def __init__(self, position):
        self.position = position
        self.g = float('inf')  # cost from start
        self.h = 0  # heuristic (estimated cost to goal)
        self.f = 0  # total cost
        self.predecessor = None

    def __lt__(self, other):
        return self.f < other.f

def is_valid(x, y):
    return 1 <= x <= 6 and 1 <= y <= 6

def calculate_cost(current, neighbor):
    if abs(current.position[0] - neighbor.position[0]) + abs(current.position[1] - neighbor.position[1]) == 2:
        return math.sqrt(2)  # diagonal movement
    else:
        return 1  # horizontal or vertical movement

def plot_grid(ax, obstacles, start, goal, path):
    for i in range(1, 7):
        for j in range(1, 7):
            if (i, j) in obstacles:
                ax.add_patch(Rectangle((i - 0.5, j - 0.5), 1, 1, facecolor='black'))
            else:
                ax.add_patch(Rectangle((i - 0.5, j - 0.5), 1, 1, edgecolor='black', facecolor='white'))

    ax.add_patch(Rectangle((start.position[0] - 0.5, start.position[1] - 0.5), 1, 1, facecolor='green'))
    ax.add_patch(Rectangle((goal.position[0] - 0.5, goal.position[1] - 0.5), 1, 1, facecolor='red'))

    if path:
        path_x, path_y = zip(*path)
        ax.plot(path_x, path_y, marker='o', color='blue')

    ax.set_xlim(0.5, 6.5)
    ax.set_ylim(0.5, 6.5)
    ax.set_aspect('equal', 'box')
    ax.invert_yaxis()

def astar(start, goal, obstacles):
    open_set = [start]
    closed_set = set()

    fig, ax = plt.subplots()

    while open_set:
        current = heapq.heappop(open_set)
        closed_set.add(current.position)

        if current.position == goal.position:
            path = []
            while current:
                path.append(current.position)
                current = current.predecessor
            path.reverse()
            
            plot_grid(ax, obstacles, start, goal, path)
            plt.show()
            
            return path

        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue

                neighbor_pos = (current.position[0] + i, current.position[1] + j)
                if is_valid(*neighbor_pos) and neighbor_pos not in obstacles and neighbor_pos not in closed_set:
                    neighbor = Node(neighbor_pos)
                    tentative_g = current.g + calculate_cost(current, neighbor)

                    if tentative_g < neighbor.g:
                        neighbor.g = tentative_g
                        neighbor.h = math.sqrt((goal.position[0] - neighbor.position[0]) ** 2 +
                                              (goal.position[1] - neighbor.position[1]) ** 2)
                        neighbor.f = neighbor.g + neighbor.h
                        neighbor.predecessor = current

                        if neighbor not in open_set:
                            heapq.heappush(open_set, neighbor)

    return None

# Define grid, obstacles, and nodes
start_node = Node((3, 4))  # Update to the coordinates of grid number 16
goal_node = Node((5, 6))   # Update to the coordinates of grid number 32
obstacles = {(2, 2), (4, 4), (5, 4), (3, 3), (4, 3), (6, 3), (3, 5), (6, 2), (3, 4)}
additional_obstacle = (6, 3)
obstacles.add(additional_obstacle)

# Run A* algorithm
astar_path = astar(start_node, goal_node, obstacles)

# Print final path
print("A* Path:", astar_path)
