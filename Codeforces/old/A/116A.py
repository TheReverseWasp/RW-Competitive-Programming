it = int(input())
answer = 0
curr = 0
for i in range(it):
    [d, u] = list(map(int, input().split(" ")))
    curr += u - d
    if curr > answer:
        answer = curr
print(answer)