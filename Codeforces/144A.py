sdrs = int(input())
sdrs_l = list(map(int, input().split()))
min_s = min(sdrs_l)
max_s = max(sdrs_l)
temp = 0
for i in range(sdrs):
    if sdrs_l[i] == max_s:
        temp = i + 0
        break
ans = temp + 0
sdrs_l = [sdrs_l[temp]] + sdrs_l[:temp] + sdrs_l[temp + 1:]
for i in range(sdrs):
    if sdrs_l[sdrs-1-i] == min_s:
        ans += i
        break
print(ans)