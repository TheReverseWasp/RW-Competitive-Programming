n, s, r = map(int, input().split())
damaged = set(map(int, input().split()))
reserved = set(map(int, input().split()))
for i in range(1,n + 1):
    if not i in damaged:
        continue
    if i in damaged:
        if i > 1:
            if i - 1 in reserved:
                reserved.remove(i - 1)
                damaged.remove(i)
            elif i in reserved:
                reserved.remove(i)
                damaged.remove(i)
            elif i < n:
                if i + 1 in reserved:
                    reserved.remove(i + 1)
                    damaged.remove(i)
        else:
            if i in reserved:
                reserved.remove(i)
                damaged.remove(i)
            elif i + 1 in reserved:
                reserved.remove(i + 1)
                damaged.remove(i)
print(len(damaged))