n, k = map(int,input().split())
problems = list(map(int,input().split()))
ini, fin = 0, n - 1
ans = 0
while ini <= fin and ini < n and fin >= 0:
    if problems[ini] <= k:
        ans+=1
        ini+=1
        continue
    if problems[fin] <= k:
        ans+=1
        fin-=1
        continue
    break
print(ans)