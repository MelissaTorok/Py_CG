import numpy as np
from scipy.spatial import distance_matrix
import networkx as nx

# Define the points
A = np.array([-1, 6])
B = np.array([-1, -1])
C = np.array([4, 7])
D = np.array([6, 7])
E = np.array([1, -1])
F = np.array([-5, 3])
P = np.array([-2, 3])

# Function to compute the minimal spanning tree length for a given \u03bb
def compute_mst_length(lambda_value):
    Q = np.array([2 - lambda_value, 3])  # Define Q based on \u03bb

    # Combine all points
    points = np.array([A, B, C, D, E, F, P, Q])

    # Compute the pairwise distance matrix
    dist_matrix = distance_matrix(points, points)

    # Create a complete graph using NetworkX
    G = nx.Graph()
    num_points = len(points)
    for i in range(num_points):
        for j in range(i + 1, num_points):
            G.add_edge(i, j, weight=dist_matrix[i, j])

    # Compute the minimum spanning tree (MST)
    mst = nx.minimum_spanning_tree(G)

    # Calculate the total weight (length) of the MST
    mst_length = sum(data['weight'] for _, _, data in mst.edges(data=True))
    return mst_length

# Find the value of \u03bb that minimizes the MST length
lambda_values = np.linspace(-10, 10, 1000)  # Search range for \u03bb
mst_lengths = [compute_mst_length(lambda_value) for lambda_value in lambda_values]

# Find the minimum length and corresponding \u03bb
min_length = min(mst_lengths)
best_lambda = lambda_values[np.argmin(mst_lengths)]

print(f"The smallest MST length is {min_length:.4f} and occurs at \u03bb = {best_lambda:.4f}")
