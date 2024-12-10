def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0 
    elif val > 0:
        return 1  
    else:
        return 2  

def graham_scan(points):
    points = sorted(points, key=lambda x: (x[1], x[0]))
    result = []
    for point in points:
        while len(result) >= 2 and orientation(result[-2], result[-1], point) != 2:
            result.pop()
        result.append(point)

    return result

points = [(0, 0), (2, 1), (1, 2), (4, 3), (3, 3), (1, 1)]
result = graham_scan(points)

print("Points:", result)
