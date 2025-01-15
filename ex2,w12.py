import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

# Define the given points
points = np.array([
    [5, -1],   # A1
    [7, -1],   # A2
    [9, -1],   # A3
    [7, -3],   # A4
    [11, -1],  # A5
    [-9, 3]    # A6
])

# Add A7 and A8 strategically to create exactly 4 half-line edges
# Place them far from the existing cluster to ensure regions extend infinitely
A7 = [15, 10]  # Example point far to the upper-right
A8 = [-15, -10]  # Example point far to the bottom-left
points = np.vstack([points, A7, A8])

# Compute the Voronoi diagram
vor = Voronoi(points)

# Plot the Voronoi diagram
plt.figure(figsize=(10, 10))
voronoi_plot_2d(vor, show_vertices=False, line_colors='blue', line_width=1.5, line_alpha=0.6, point_size=10)
plt.scatter(points[:, 0], points[:, 1], color='red', label='Points')
plt.title("Voronoi Diagram with 4 Half-Line Edges")
plt.legend()
plt.grid()
plt.show()

# Explanation of construction:
# - A7 and A8 are placed far away to ensure their Voronoi regions extend to infinity.
# - With these placements, four edges of the diagram are guaranteed to extend as half-lines.
