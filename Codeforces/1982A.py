tc = int(input())
for _ in range(tc):
    a1,b1 = map(int,input().split())
    a2,b2 = map(int,input().split())
    ###
    if (b1 <= a1 and a1 <= b2 and b1 <= a2 and a2 <= b2) or (a1 <= b1 and b1 <= a2 and a1 <= b2 and b2 <= a2):
        print("NO")
    else:
        print("YES")