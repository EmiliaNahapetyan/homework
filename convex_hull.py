def convex_hull(points):
    points = sorted(points)
    hull = []

    for i in points:
        while len(hull) >= 2 and cross_product(hull[-2], hull[-1], i) <= 0:
            hull.pop()
        hull.append(i)

    lower_hull_size = len(hull)
    for i in reversed(points):
        while len(hull) > lower_hull_size and cross_product(hull[-2], hull[-1], i) <= 0:
            hull.pop()
        hull.append(i)

    return hull[:-1]

def cross_product(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p2[1]) - (p2[1] - p1[1]) * (p3[0] - p2[0])

points = [(0, 0), (1, 1), (2, 2), (2, 0), (2, 4), (3, 3), (4, 2)]
hull = convex_hull(points)
print("Convex Hull:", hull)
