import matplotlib.pyplot as plt
from shapely.geometry import Polygon, Point
from shapely.ops import triangulate

# Step 1: Define the vertices of the polygon
vertices = [
    (4, 4), (5, 6), (6, 4), (7, 4), (9, 6), (11, 6),  # Top half
    (11, -6), (9, -6), (7, -4), (6, -4), (5, -6), (4, -4)  # Bottom half (symmetric)
]

# Step 2: Create the polygon
polygon = Polygon(vertices)

# Step 3: Triangulate the polygon
triangles = triangulate(polygon)

# Step 4: Visualize the polygon and the triangulation
fig, ax = plt.subplots()
for triangle in triangles:
    x, y = triangle.exterior.xy
    ax.fill(x, y, alpha=0.4, edgecolor='black')

# Draw the original polygon
x, y = polygon.exterior.xy
ax.plot(x, y, color="blue", linewidth=2, label="Polygon")

# Step 5: Apply the Art Gallery Theorem
# According to the theorem, we need at most floor(n/3) cameras
n = len(vertices)
num_cameras = n // 3

# Step 6: Choose camera positions (using vertex coloring)
# Simple approach: Pick 1 out of every 3 vertices
camera_positions = vertices[::3]
camera_x, camera_y = zip(*camera_positions)

# Plot the cameras
ax.scatter(camera_x, camera_y, color="red", label="Cameras", zorder=5)

# Annotations
for i, (x, y) in enumerate(vertices, start=1):
    ax.text(x, y, f"P{i}", fontsize=10, color="black")

# Step 7: Finalize the plot
ax.set_aspect('equal')
ax.legend()
plt.title("Art Gallery Theorem: Triangulation and Camera Placement")
plt.show()
