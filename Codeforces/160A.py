coins = int(input())
l1 = list(map(int, input().split()))
l1.sort()
l2 = [0]
for i in l1:
    l2.append(l2[-1] + i)

c = 0
for i in range(len(l2) - 2, -1, -1):
    c += 1
    if l2[-1] - l2[i] > l2[i]:
        break
print(c)
