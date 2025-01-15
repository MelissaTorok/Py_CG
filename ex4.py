def cross_product(o, a, b):
    """
    Compute the cross product of vectors OA and OB.
    A positive value indicates a left turn (counter-clockwise),
    negative indicates a right turn (clockwise),
    and zero indicates collinear points.
    """
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def jarvis_march(points):
    """
    Perform the Jarvis March algorithm to compute the convex hull.
    Returns the convex hull as a list of points in counter-clockwise order.
    """
    # Step 1: Find the leftmost point (smallest x; tie-breaker: smallest y)
    start = min(points, key=lambda p: (p[0], p[1]))
    hull = []
    current = start

    while True:
        hull.append(current)
        next_point = points[0]  # Initialize the next point as an arbitrary point

        for candidate in points:
            # Skip the current point itself
            if candidate == current:
                continue

            # Determine if candidate is a better choice for the next point
            direction = cross_product(current, next_point, candidate)
            if next_point == current or direction > 0 or (direction == 0 and
                ((candidate[0] - current[0])**2 + (candidate[1] - current[1])**2 >
                 (next_point[0] - current[0])**2 + (next_point[1] - current[1])**2)):
                next_point = candidate

        current = next_point
        # Break when we return to the start point
        if current == start:
            break

    return hull

# Define the points
points = [(2, 0), (0, 3), (-4, 0), (4, 2), (5, 1)]

# Compute the convex hull
convex_hull = jarvis_march(points)
print("Convex Hull:", convex_hull)
