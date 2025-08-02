tc = int(input())
for __ in range(tc):
    a,b,c = map(int,input().split())
    dist = abs(a-b)
    if dist == 1:
        print(-1)
        continue
    maxo = dist * 2
    if c > maxo or a > maxo or b > maxo:
        print(-1)
        continue
    if c + dist > maxo:
        print((c + dist) % maxo)
    else:
        print(c+dist)