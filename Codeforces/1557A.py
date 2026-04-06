tc = int(input())
for __ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    maxo = max(a)
    suma = sum(a)
    answer = (suma-maxo)/(n-1) + maxo
    print(f"{answer:.10f}") 
