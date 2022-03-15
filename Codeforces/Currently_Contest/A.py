import re

t = int(input())
while t:
    t-=1
    s = input()
    temp = input()
    pos = [m.start() for m in re.finditer(temp, s)]
    flag = False
    for p in pos:
        if p % 2 == 0:
            print("YES")
            flag = True
            break
    if not flag:
        print("NO")
