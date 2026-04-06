tc = int(input())
for _ in range(tc):
    n = int(input())
    s = input()
    if "2026" in s or not "2025" in s:
        print(0)
    else:
        print(1)