cups = sum(list(map(int,input().split())))
medals = sum(list(map(int,input().split())))
shelves = int(input())
shelves -= cups // 5 + (1 if cups % 5 != 0 else 0)
shelves -= medals // 10 + (1 if medals % 10 != 0 else 0)
if shelves >= 0:
    print("YES")
else:
    print("NO")