def solve():
    a,b,c = map(int,input().split())
    a,c=a+min(b-a,c-b),c-min(b-a,c-b)
    if a == b and b == c:
        print("YES")
    else:
        if a == b and (c-b) % 3 != 0:
            print("NO")
        elif (c-b) == 0:
            print("NO")
        else:
            print("YES")


tc=int(input())
for _ in range(tc):
    solve()