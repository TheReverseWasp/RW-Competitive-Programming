n = int(input())
a = list(map(int,input().split()))
ans = "Yes"
for i in range(1,n):
    if a[i-1] < a[i]:
       continue
    ans = "No"
    break
print(ans)
