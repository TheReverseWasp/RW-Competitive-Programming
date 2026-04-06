n, k = map(int, input().split())
a = list(map(int, input().split()))

for elem in a:
    if elem % k == 0:
        print(elem // k, end = " ")
print()