t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    a = set(list(map(int,input().split())))
    b = set(list(map(int,input().split())))
    interest = a.intersection(b)
    if len(interest) > 0:
        print("YES")
        for elem in interest:
            print(1,elem)
            break
    else:
        print("NO")