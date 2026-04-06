n = int(input())
answer = list()
while n > 0:
    if n <= 3:
        answer.append(n + 0)
        n -= n
        continue
    answer.append(2)
    n-=2
print(len(answer))
for elem in answer:
    print(elem, end=" ")
print()
