n = int(input())
stp_l = list(map(int,input().split()))
ans = 1
temp = 1
for i in range(1, n):
    if stp_l[i] >= stp_l[i-1]:
        temp += 1
        if ans < temp:
            ans = temp + 0
    else:
        temp = 1
print(ans)