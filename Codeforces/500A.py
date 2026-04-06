n,t = map(int,input().split())
portals = list(map(int,input().split()))
i = 0
actual = 1
visited = set([actual])
while i < n-1:
    actual += portals[i]
    i+= portals[i]
    visited.add(actual)
if t in visited:
    print("YES")
else:
    print("NO")
