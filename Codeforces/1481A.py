tc = int(input())
for _ in range(tc):
    px, py = map(int,input().split())
    s = input()
    min_x, min_y, max_x, max_y, x, y = 0,0,0,0,0,0
    for elem in s:
        if elem == "U":
            max_y+=1
        elif elem == "D":
            min_y-=1
        elif elem == "R":
            max_x+=1
        else:
            min_x-=1
    if min_x <= px and px <= max_x and min_y <= py and py <= max_y:
        print("YES")
    else:
        print("NO")