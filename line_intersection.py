def line_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    print('d =', d)
    
    if d == 0:
        return None

    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / d
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / d

    return px, py

x1, y1 = 1, 1
x2, y2 = 4, 4
x3, y3 = 1, 8
x4, y4 = 2, 4

intersection = line_intersection(x1, y1, x2, y2, x3, y3, x4, y4)

if intersection:
    print(f"The lines intersect at: {intersection}")
else:
    print("The lines do not intersect.")
