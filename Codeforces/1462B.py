tc = int(input())
for __ in range(tc):
    n = int(input())
    s = input()
    flag = False
    if s.startswith("2020") or s.endswith("2020"):
        flag = True
    elif s.startswith("2") and s.endswith("020"):
        flag = True
    elif s.startswith("20") and s.endswith("20"):
        flag = True
    elif s.startswith("202") and s.endswith("0"):
        flag = True
    print("YES" if flag else "NO")