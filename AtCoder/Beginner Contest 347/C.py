n, a, b = map(int, input().split())

d = list(map(int, input().split()))

s = set([0])
for j in range(1, len(d)):
    acum = d[j] - d[0]
    s.add(acum % (a + b))

s2 = set([a - 1])
for j in range(1, len(d)):
    acum = d[j]
    s2.add(acum % (a + b))

range_max = max(list(s))
other_range_max = max(list(s2))

if range_max < a or other_range_max < a:
    print("Yes")
else:
    print("No")