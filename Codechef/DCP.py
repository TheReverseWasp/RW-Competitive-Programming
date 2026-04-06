n, m = map(int, input().split())
c = list(map(int, input().split()))
while m:
    m-=1
    C, elems = map(int, input().split())
    eq = list(map(int, input().split()))
    for i in range(0,len(eq),2):
        c[eq[i + 1] - 1] += eq[i] * c[C - 1]
    c[C - 1] = 0
for elem in c:
    print(elem%1000000007)
