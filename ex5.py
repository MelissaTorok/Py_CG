def cross_product(o, a, b):
    """
    A positive value indicates a left turn,
    a negative value indicates a right turn,
    and zero indicates collinear points.
    """
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def lower_hull(points):
    """
    Determine the lower edge of the convex hull using Graham's scan / Andrew's monotone chain.
    """
    points = sorted(points)

    lower = []
    for p in points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    return lower

points = [
    (1, 11), (2, 7), (3, 8), (4, 10), (5, 7), (6, 7), (7, 11)
]

# Compute the lower edge of the convex hull
lower_edge = lower_hull(points)
print("Lower Edge of Convex Hull:", lower_edge)
