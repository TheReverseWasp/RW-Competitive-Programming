tc = int(input())
while(tc):
    h, v = set(), set()
    vtx = int(input())
    while vtx:
        a, b = map(int, input().split())
        h.add(a)
        v.add(b)
        vtx-=1
    print(len(h)+len(v))

    tc-=1
