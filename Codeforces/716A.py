n,c=map(int,input().split())
t=list(map(int,input().split()))
lasto = -1
consecutive = 0
for i in range(n-1, -1, -1):
    if lasto == -1:
        lasto = t[i]
        consecutive += 1
        continue
    if t[i+1] - t[i] <= c:
        consecutive += 1
        continue
    else:
        break
print(consecutive)