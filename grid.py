import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import RegularPolygon

# Define grid size and obstacles
grid_size = 6
obstacles = [2, 10, 11, 20, 21, 27, 33]

# Create a matrix to represent the grid
grid = np.zeros((grid_size, grid_size))

# Mark obstacles
for obstacle in obstacles:
    row = (obstacle - 1) // grid_size
    col = (obstacle - 1) % grid_size
    grid[row, col] = 1

# Mark start and target positions
start_position = 5
target_position = 32
start_row, start_col = (start_position - 1) // grid_size, (start_position - 1) % grid_size
target_row, target_col = (target_position - 1) // grid_size, (target_position - 1) % grid_size

grid[start_row, start_col] = 2  # Mark start with 2
grid[target_row, target_col] = 3  # Mark target with 3

# Initialize the path list
path_taken = [(start_row, start_col)]

# Calculate the path without animation
alpha_values = np.linspace(0, 1, num=100)
for alpha in alpha_values:
    new_row = int((1 - alpha) * start_row + alpha * target_row)
    new_col = int((1 - alpha) * start_col + alpha * target_col)
    path_taken.append((new_row, new_col))

# Set up the figure and axis
fig, ax = plt.subplots()
ticks = np.arange(-0.5, grid_size, 1)
plt.xticks(ticks, [])
plt.yticks(ticks, [])

# Add grid lines
plt.grid(True, which='both', color='black', linewidth=1.5)

# Add labels
for i in range(grid_size):
    for j in range(grid_size):
        value = int(grid[i, j])
        if value != 0:  # If not an empty cell
            plt.text(j, i, value, ha='center', va='center', fontsize=10)

plt.title('Grid Visualization')

# Plot the path
path_taken = np.array(path_taken)
plt.plot(path_taken[:, 1], path_taken[:, 0], marker='o', color='red', label='Path Taken')
plt.legend()

# Show the plot
plt.show()

# Print out the path taken
print("Path taken:")
for position in path_taken:
    print(position)
