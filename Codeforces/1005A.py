n = int(input())
a = list(map(int,input().split()))
ans = list()
prev = 0
acum = 0
for idx in range(n):
    if a[idx] <= prev:
        prev = 1
        ans.append(str(acum))
        acum = 1
    else:
        acum+=1
        prev = a[idx] + 0
ans.append(str(acum))
print(len(ans))
print(" ".join(ans))