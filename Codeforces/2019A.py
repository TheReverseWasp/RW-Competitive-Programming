tc = int(input())

for _ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    even, odd = [0,0], [0,0+0]
    for i in range(n):
        if i % 2 == 0:
            even[0] = max(a[i], even[0])
            even[1] += 1
        else:
            odd[0] = max(a[i], odd[0])
            odd[1] += 1
    print(max(sum(even), sum(odd)))