tc = int(input())
for _ in range(tc):
    r,c = map(int,input().split())
    if r == 1 or c == 1 or (r == 2 and c == 2):
        print("YES")
    else:
        print("NO")