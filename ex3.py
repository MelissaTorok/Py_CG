def cross_product(o, a, b):
    """Calculate the cross product of vectors OA and OB.
    A positive cross product indicates a counter-clockwise turn,
    a negative cross product indicates a clockwise turn,
    and zero indicates collinear points."""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_hull(points):
    """Compute the convex hull of a set of 2D points using Andrew's monotone chain algorithm.
    The output is a list of vertices of the convex hull in counter-clockwise order."""
    # Step 1: Sort points lexicographically (by x, then by y)
    points = sorted(points)

    # Step 2: Build the lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()  # Remove last point if it doesn't make a left turn
        lower.append(p)

    # Step 3: Build the upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()  # Remove last point if it doesn't make a left turn
        upper.append(p)

    # Remove the last point of each half because it's repeated
    return lower[:-1] + upper[:-1]

# Given points
points = [
    (4, 2), (7, 1), (-3, 5), (3, 6), (-4, -4), (-1, 1), (2, -6)
]

# Compute the convex hull
hull = convex_hull(points)
print("Convex Hull:", hull)
