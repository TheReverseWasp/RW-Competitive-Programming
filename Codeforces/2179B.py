tc=int(input())
for _ in range(tc):
    f = int(input())
    a = list(map(int,input().split()))
    suma = sum([abs(a[i] - a[i+1]) for i in range(f - 1)])
    new_min = suma + 0
    for i in range(1, f-1):
        new_min = min(suma - abs(a[i-1] - a[i]) - abs(a[i] - a[i+1]) + abs(a[i-1] - a[i+1]), new_min)
    new_min = min(new_min, suma - abs(a[-1] - a[-2]))
    new_min = min(new_min, suma - abs(a[0] - a[1]))
    print(new_min)