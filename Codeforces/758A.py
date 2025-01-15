n = int(input())
h_l = list(map(int,input().split()))
temp = max(h_l)
ans = 0
for elem in h_l:
    ans += temp - elem
print(ans)