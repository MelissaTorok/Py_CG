import matplotlib.pyplot as plt

# Step 1: Define the vertices of the polygon and an interior point
vertices = [(0, 0), (4, 0), (2, 3), (2, 1)]  # Vertices: A, B, C, D
labels = ['A', 'B', 'C', 'D']  # Labels for points

# Step 2: Define the edges of the triangulation
edges = [
    (0, 1),  # Edge AB
    (1, 2),  # Edge BC
    (2, 0),  # Edge CA
    (0, 3),  # Edge AD
    (1, 3),  # Edge BD
    (2, 3),  # Edge CD
]  # Total: 7 edges

# Step 3: Define the triangles (for coloring and visualization)
triangles = [
    (0, 1, 3),  # Triangle ABD
    (1, 2, 3),  # Triangle BCD
    (2, 0, 3),  # Triangle CAD
]

# Step 4: Plot the triangulation
fig, ax = plt.subplots()
for edge in edges:
    x_coords = [vertices[edge[0]][0], vertices[edge[1]][0]]
    y_coords = [vertices[edge[0]][1], vertices[edge[1]][1]]
    ax.plot(x_coords, y_coords, color='black')

# Plot the vertices
for i, (x, y) in enumerate(vertices):
    ax.scatter(x, y, color='blue', zorder=5)
    ax.text(x, y, f" {labels[i]}", fontsize=12, color="black")

# Fill triangles with different colors (3-colorable)
colors = ['lightblue', 'lightgreen', 'lightpink']
for i, triangle in enumerate(triangles):
    x_coords = [vertices[triangle[j]][0] for j in range(3)]
    y_coords = [vertices[triangle[j]][1] for j in range(3)]
    ax.fill(x_coords, y_coords, color=colors[i], alpha=0.5)

# Finalize the plot
ax.set_aspect('equal')
plt.title("Triangulation with 3 Triangles and 7 Edges (3-Colorable)")
plt.show()
