r,c=map(int,input().split())
mat = list()
madam=set()
for y in range(r):
    mat.append(input())
    for x in range(c):
        if mat[y][x]=="S":
            madam.add((y,x))

prohibited_r, prohibited_c, recorrido = set(), set(), 0
for (y,x) in madam:
    prohibited_r.add(y)
    prohibited_c.add(x)
for x in range(r):
    for y in range(c):
        if y in prohibited_c and x in prohibited_r:
            continue
        recorrido+=1

print(recorrido)