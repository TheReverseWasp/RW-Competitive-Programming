tc = int(input())
for __ in range(tc):
    b,c,h = map(int,input().split())
    condiments = c + h
    levels = 0
    if condiments < b - 1:
        levels = condiments + condiments + 1
    else:
        levels = b + b - 1
    print(levels)