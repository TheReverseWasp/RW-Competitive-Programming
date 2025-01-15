pbms, time = map(int, input().split())
av_time = 240 - time
ans = 0
for i in range(pbms):
    if av_time - (i + 1) * 5 >= 0:
        ans += 1
        av_time -= (i + 1) * 5 
    else:
        break
print(ans)