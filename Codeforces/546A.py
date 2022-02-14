[k, n, w] = list(map(int, input().split()))
print(0 if int((w *(w + 1)) / 2) * k - n <= 0 else int((w *(w + 1)) / 2) * k - n)
