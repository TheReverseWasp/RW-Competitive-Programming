tc = int(input())
for _ in range(tc):
    n = int(input())
    s = input()
    if "ab" in s or "ba" in s:
        pos = s.find("ab")
        if pos == -1:
            pos = s.find("ba")
        print(pos +1, pos + 2)
    else:
        print(-1, -1)