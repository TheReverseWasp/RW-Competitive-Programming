sz = input()
cad = input()
answer = 0
for i in range(1, len(cad)):
    if cad[i] == cad[i - 1]:
        answer += 1
print(answer)