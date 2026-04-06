tc=int(input())
for _ in range(tc):
    n,m,r,c=map(int,input().split())
    black_col = set()
    black_row = set()
    ans = 0
    found = False
    for y in range(n):
        temp = input()
        for x, val in enumerate(temp):
            if val == "B":
                if r == y + 1 and c == x + 1:
                    ans = 0
                    found = True
                else:
                    black_col.add(x+1)
                    black_row.add(y+1)
    if found:
        print(0)
        continue
    if len(black_col) == 0:
        print(-1)
        continue
    if r in black_row or c in black_col:
        print(1)
    else:
        print(2)