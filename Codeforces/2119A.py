tc = int(input())
for _ in range(tc):
    a,b,x,y = map(int,input().split())
    if a > b:
        if a-b == 1 and a % 2 == 1:
            print(y)
            continue
        else:
            print(-1)
            continue
    elif a == b:
        print(0)
        continue
    else:
        ans = 0
        while a < b:
            if a % 2 == 0:
                ans+= min(x,y)
            elif a%2 == 1:
                ans+=x
            a+=1
        print(ans)
        continue