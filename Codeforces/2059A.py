tc = int(input())
for _ in range(tc):
    input()
    s1 = set(list(map(int, input().split())))
    s2 = set(list(map(int, input().split())))
    if len(s1) * len(s2) >= 3:
        print("YES")
    else:
        print("NO")