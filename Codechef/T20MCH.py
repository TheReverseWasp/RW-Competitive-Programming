r, o, c =map(int, input().split())
temp = (20 - o) * 6 * 6
if c + temp > r:
    print("YES")
else:
    print("NO")
