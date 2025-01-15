import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, Delaunay, voronoi_plot_2d, delaunay_plot_2d

# Define the points
points = np.array([
    [3, -5],  # A
    [-6, 6],  # B
    [6, -4],  # C
    [5, -5],  # D
    [9, 10]   # E
])

# Compute the Voronoi diagram
vor = Voronoi(points)

# Compute the Delaunay triangulation
del_tri = Delaunay(points)

# Plotting the Voronoi diagram
plt.figure(figsize=(10, 10))
voronoi_plot_2d(vor, show_vertices=False, line_colors='blue', line_width=1.5, line_alpha=0.6, point_size=10)
plt.scatter(points[:, 0], points[:, 1], color='red', label='Points')
plt.title("Voronoi Diagram")
plt.legend()
plt.grid()
plt.show()

# Plotting the Delaunay triangulation
plt.figure(figsize=(10, 10))
delaunay_plot_2d(del_tri)
plt.scatter(points[:, 0], points[:, 1], color='red', label='Points')
plt.title("Delaunay Triangulation")
plt.legend()
plt.grid()
plt.show()
