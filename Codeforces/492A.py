n = int(input())
a = 1
acum = a + 0
while n - acum >= 0:
    a += 1
    n -= acum
    acum += a
print(a - 1)
