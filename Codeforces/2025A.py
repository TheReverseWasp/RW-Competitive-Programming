tc = int(input())
for _ in range(tc):
    a = input()
    b = input()
    ans = 0
    i=0
    while i < min(len(a), len(b)):
        if a[i] == b[i]:
            i+=1
            continue
        else:
            break
    if i == 0:
        print(len(a)+len(b))
    else:
        print(i + 1 + (len(a) - i + len(b) - i))