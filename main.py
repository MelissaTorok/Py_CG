import numpy as np
from scipy.spatial import ConvexHull

A = (3, -3)
B = (3, 3)
C = (-3, -3)
D = (-3, 3)

def calculate_M(lambda_val):
    return (2 - lambda_val, 3 + lambda_val)

def points_on_convex_hull(lambda_val):
    M = calculate_M(lambda_val)

    points = np.array([A, B, C, D, M])

    hull = ConvexHull(points)

    hull_points = points[hull.vertices]

    return len(hull_points)

lambda_values = [-7, 2]
for lambda_val in lambda_values:
    num_points = points_on_convex_hull(lambda_val)
    print(f"Lambda = {lambda_val}: {num_points} points on the convex hull border.")
