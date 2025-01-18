import matplotlib.pyplot as plt

# Step 1: Define the vertices
vertices = [
    (0, 0),  # A
    (4, 0),  # B
    (5, 3),  # C
    (2, 5),  # D
    (-1, 3), # E
    (2, 2),  # F (Interior Point)
]
labels = ['A', 'B', 'C', 'D', 'E', 'F']

# Step 2: Define the edges for the full triangulation
edges = [
    (0, 1), (1, 2), (2, 3), (3, 4), (4, 0),  # Outer pentagon edges
    (0, 5), (1, 5), (2, 5), (3, 5), (4, 5)  # Interior connections to F
]  # Total: 10 edges (outer) + 5 edges (interior) = 12

# Step 3: Subset triangulation (4 points: A, B, C, F)
subset_edges = [
    (0, 1), (1, 2), (2, 0),  # Outer triangle edges
    (0, 5), (2, 5)           # Connections to F
]  # Total: 5 edges

# Step 4: Plot the full triangulation
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# Full triangulation
for edge in edges:
    x_coords = [vertices[edge[0]][0], vertices[edge[1]][0]]
    y_coords = [vertices[edge[0]][1], vertices[edge[1]][1]]
    ax[0].plot(x_coords, y_coords, color='black')

# Plot vertices for the full triangulation
for i, (x, y) in enumerate(vertices):
    ax[0].scatter(x, y, color='blue', zorder=5)
    ax[0].text(x, y, f" {labels[i]}", fontsize=10, color="black")

ax[0].set_title("Full Triangulation with 6 Points (12 Edges)")
ax[0].set_aspect('equal')

# Subset triangulation (A, B, C, F)
for edge in subset_edges:
    x_coords = [vertices[edge[0]][0], vertices[edge[1]][0]]
    y_coords = [vertices[edge[0]][1], vertices[edge[1]][1]]
    ax[1].plot(x_coords, y_coords, color='black')

# Plot vertices for the subset triangulation
for i, (x, y) in enumerate(vertices[:4] + [vertices[5]]):  # Only A, B, C, F
    ax[1].scatter(x, y, color='blue', zorder=5)
    ax[1].text(x, y, f" {labels[i]}", fontsize=10, color="black")

ax[1].set_title("Subset Triangulation (4 Points, 5 Edges)")
ax[1].set_aspect('equal')

# Finalize the plot
plt.show()
