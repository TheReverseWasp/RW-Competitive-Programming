r, n = map(int, input().split())
d = {}
for i in range(n):
    d[int(input())] = True

f = False
for i in range(1, r + 1):
    if not i in d:
        print(i)
        f = True
        break
if f == False:
    print("too late")