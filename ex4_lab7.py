import matplotlib.pyplot as plt

# Step 1: Define the vertices of the polygon
vertices = [
    (0, 0),  # A
    (4, 0),  # B
    (6, 3),  # C
    (4, 6),  # D
    (0, 6),  # E
    (-2, 3), # F
    (2, 3),  # G (Interior Point)
]
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# Step 2: Define the edges of the triangulation
edges = [
    (0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0),  # Outer edges of the hexagon
    (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6)   # Connections to the interior point G
]  # Total edges = 14

# Step 3: Define the triangles (for coloring)
triangles = [
    (0, 1, 6),  # Triangle ABG
    (1, 2, 6),  # Triangle BCG
    (2, 3, 6),  # Triangle CDG
    (3, 4, 6),  # Triangle DEG
    (4, 5, 6),  # Triangle EFG
    (5, 0, 6),  # Triangle FAG
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
    ax.fill(x_coords, y_coords, color=colors[i % 3], alpha=0.5)

# Finalize the plot
ax.set_aspect('equal')
plt.title("Triangulation with 14 Edges (3-Colorable)")
plt.show()
