import math

def get_area(a,b):
    return abs(a-b)
for _ in range(int(input())):
    n = int(input())
    a=list(map(int,input().split()))
    areas = set()
    for idx_1, pos_1 in enumerate(a):
        for idx_2, pos_2 in enumerate(a):
            if idx_1 != idx_2:
                areas.add(get_area(pos_1,pos_2))
    print(len(areas))