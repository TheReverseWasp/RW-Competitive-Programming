n, k = map(int, input().split())
odd_n = n//2
if n % 2 == 1:
    odd_n += 1
if k > odd_n:
    print((k-odd_n)*2)
else:
    print(k*2-1)