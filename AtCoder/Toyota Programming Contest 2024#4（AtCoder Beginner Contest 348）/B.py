import math

def dist(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

n = int(input())
points = list()

for i in range(n):
    points.append(tuple(map(int, input().split())))

for i in range(n):
    longest_distance = 0
    farthest_point = ""
    for j in range(n):
        if j != i:
            temp = dist(points[i], points[j])
            if temp > longest_distance:
                longest_distance = temp + 0
                farthest_point = j + 0
    print(farthest_point + 1)
    