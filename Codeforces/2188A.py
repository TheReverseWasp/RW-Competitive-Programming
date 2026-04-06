tc = int(input())
for _ in range(tc):
    n = int(input())
    odd = n // 2 + 1
    even = odd - 1
    for i in range(1,n+1):
        if i % 2 == 1:
            print(odd,end=" ")
            odd += 1
        else:
            print(even, end=" ")
            even-=1
    print()