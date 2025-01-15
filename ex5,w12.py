import numpy as np
from scipy.spatial import Delaunay, Voronoi
import matplotlib.pyplot as plt

# Define the two sets of points
M1 = np.array([
    [0, 0],
    [1, 0],
    [0, 1],
    [1, 1]   
])

M2 = np.array([
    [0, 0],  # Point 1
    [2, 0],  # Point 2
    [0, 2]   # Point 3
])

# Function to compute triangulation and Voronoi diagram properties
def analyze_points(points):
    # Compute Delaunay triangulation
    delaunay = Delaunay(points)

    # Number of triangles in the triangulation
    num_triangles = len(delaunay.simplices)

    # Number of edges in the triangulation
    edges = set()
    for simplex in delaunay.simplices:
        for i in range(len(simplex)):
            for j in range(i + 1, len(simplex)):
                edges.add(tuple(sorted([simplex[i], simplex[j]])))
    num_edges = len(edges)

    # Compute Voronoi diagram
    voronoi = Voronoi(points)

    # Count the number of half-line edges in the Voronoi diagram
    num_half_lines = sum(1 for ridge in voronoi.ridge_vertices if -1 in ridge)

    return num_triangles, num_edges, num_half_lines

# Analyze M1
triangles_M1, edges_M1, half_lines_M1 = analyze_points(M1)
print("Set M1:")
print(f"Number of triangles: {triangles_M1}")
print(f"Number of edges in triangulation: {edges_M1}")
print(f"Number of half-line edges in Voronoi diagram: {half_lines_M1}")

# Analyze M2
triangles_M2, edges_M2, half_lines_M2 = analyze_points(M2)
print("\nSet M2:")
print(f"Number of triangles: {triangles_M2}")
print(f"Number of edges in triangulation: {edges_M2}")
print(f"Number of half-line edges in Voronoi diagram: {half_lines_M2}")

# Plot M1 and M2 with their Delaunay triangulations
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Plot M1
axes[0].triplot(M1[:, 0], M1[:, 1], Delaunay(M1).simplices, color='blue')
axes[0].scatter(M1[:, 0], M1[:, 1], color='red')
axes[0].set_title("M1: Delaunay Triangulation")
axes[0].grid(True)

# Plot M2
axes[1].triplot(M2[:, 0], M2[:, 1], Delaunay(M2).simplices, color='blue')
axes[1].scatter(M2[:, 0], M2[:, 1], color='red')
axes[1].set_title("M2: Delaunay Triangulation")
axes[1].grid(True)

plt.tight_layout()
plt.show()
