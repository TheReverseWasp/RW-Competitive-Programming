n, k = map(int, input().split(" "))
l = list(map(int, input().split(" ")))
acum = 0
score = l[k - 1]
while l[k - 1] == score and k < n:
    k += 1
if l[k - 1] != score:
    k -= 1
for i in range(k - 1, -1, -1):
    if l[i] != 0:
        acum += 1
print(acum)