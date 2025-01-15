import numpy as np
from scipy.spatial import Delaunay

A = np.array([1, 1])
B = np.array([1, -1])
C = np.array([-1, -1])
D = np.array([-1, 1])
E = np.array([0, -2])

def analyze_triangulation(lambda_value):
    M = np.array([0, lambda_value])

    points = np.array([A, B, C, D, E, M])

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

    return num_triangles, num_edges

# Test the function for a specific \u03bb
lambda_value = 0.5
num_triangles, num_edges = analyze_triangulation(lambda_value)
print(f"For \u03bb = {lambda_value}:")
print(f"Number of triangles: {num_triangles}")
print(f"Number of edges: {num_edges}")

# Optionally, iterate over multiple \u03bb values
lambda_values = np.linspace(-10, 10, 10)
for lambda_value in lambda_values:
    num_triangles, num_edges = analyze_triangulation(lambda_value)
    print(f"\u03bb = {lambda_value:.2f}, Triangles: {num_triangles}, Edges: {num_edges}")
