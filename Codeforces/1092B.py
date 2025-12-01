n = int(input())
a = list(map(int,input().split()))
a.sort()
acum = 0
for i in range(0,n,2):
    acum += a[i+1] - a[i]
print(acum)