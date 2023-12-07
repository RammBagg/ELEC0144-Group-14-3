import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import RegularPolygon
from matplotlib.animation import FuncAnimation

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

# Set up the figure and axis
fig, ax = plt.subplots()
ticks = np.arange(-0.5, grid_size, 1)
plt.xticks(ticks, [])
plt.yticks(ticks, [])

# Initialize the triangle
triangle = RegularPolygon((start_col, start_row), numVertices=3, radius=0.4, orientation=np.radians(-90), color='black')
ax.add_patch(triangle)

# Add grid lines
plt.grid(True, which='both', color='black', linewidth=1.5)

# Add labels
for i in range(grid_size):
    for j in range(grid_size):
        value = int(grid[i, j])
        if value != 0:  # If not an empty cell
            plt.text(j, i, value, ha='center', va='center', fontsize=10)

plt.title('Grid Visualization')

# Animation function
def update(frame):
    global triangle  # Declare triangle as a global variable

    # Calculate the new position of the triangle
    alpha = frame / 100.0
    new_row = int((1 - alpha) * start_row + alpha * target_row)
    new_col = int((1 - alpha) * start_col + alpha * target_col)

    # Remove the old triangle
    triangle.remove()

    # Create a new triangle at the new position
    triangle = RegularPolygon((new_col, new_row), numVertices=3, radius=0.4, orientation=np.radians(-90), color='black')
    ax.add_patch(triangle)

    return triangle,

# Create animation
animation = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.show()
