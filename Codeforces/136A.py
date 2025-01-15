frnds = int(input())
frnds_l = list(map(int, input().split()))
answer = list()
for i in range(frnds):
    answer.append(0)
for i in range(frnds):
    answer[frnds_l[i] - 1] = str(i + 1)
print(" ".join(answer))