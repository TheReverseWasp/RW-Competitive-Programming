[l, b] = list(map(int, input().split()))
acum = 0
while l <= b:
    acum += 1
    l *= 3
    b *= 2
print(acum)