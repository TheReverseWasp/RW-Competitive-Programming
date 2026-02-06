tc=int(input())
for _ in range(tc):
    n,s,x=map(int,input().split())
    a = sum(list(map(int,input().split())))
    if a < s:
        if (s - a) % x == 0:
            print("YES")
        else:
            print("NO")
    elif a == s:
        print("YES")
    else:
        print("NO")