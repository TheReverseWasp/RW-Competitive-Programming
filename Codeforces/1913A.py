def is_greater(a,b):
    if b.startswith("0"):
        return False
    if int(a) < int(b):
        return True
    return False

tc=int(input())
for _ in range(tc):
    s = input()
    founded = False
    for i in range(len(s) - 1):
        a = s[:i + 1]
        b = s[i+1:]
        if is_greater(a,b):
            founded = True
            print(a,b)
            break
    if not founded:
        print(-1)