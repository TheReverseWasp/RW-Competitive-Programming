tc = int(input())
for i in range(tc):
    c = int(input())
    d = {}
    for i in range(c):
        d[input()] = True
    a = 0
    for k, v in d.items():
        a += 1
    print(a)
