n = int(input())
l = list(map(int,input().split()))
answer = 1
consecutive = 1
for i in range(1,n):
    if l[i-1] < l[i]:
        consecutive += 1
    else:
        consecutive = 1
    if consecutive > answer:
        answer = consecutive + 0

print(answer)