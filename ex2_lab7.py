import matplotlib.pyplot as plt
from shapely.geometry import Polygon, Point
from shapely.ops import triangulate

# Step 1: Define the vertices of the polygon
vertices = [(5, 0), (3, 2), (-1, 2), (-3, 0), (-1, -2), (3, -2)]

# Step 2: Create the polygon
polygon = Polygon(vertices)

# Step 3: Triangulate the polygon
triangles = triangulate(polygon)

# Step 4: Visualize the polygon and triangulation
fig, ax = plt.subplots()
for triangle in triangles:
    x, y = triangle.exterior.xy
    ax.fill(x, y, alpha=0.4, edgecolor='black')

# Draw the original polygon
x, y = polygon.exterior.xy
ax.plot(x, y, color="blue", linewidth=2, label="Polygon")

# Step 5: Apply the Art Gallery Theorem
# For n = 6 vertices, at most floor(n/3) = 2 cameras are needed.
# For this variant, we place a single camera at a key vertex.
camera_position = vertices[0]  # Place camera at P1
camera_x, camera_y = camera_position

# Plot the camera
ax.scatter(camera_x, camera_y, color="red", label="Camera (P1)", zorder=5)

# Annotate vertices
for i, (x, y) in enumerate(vertices, start=1):
    ax.text(x, y, f"P{i}", fontsize=10, color="black")

# Step 6: Finalize the plot
ax.set_aspect('equal')
ax.legend()
plt.title("Art Gallery Theorem: Single Camera Placement (First Variant)")
plt.show()
