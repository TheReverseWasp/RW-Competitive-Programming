it = int(input())
answer = 0
for i in range(it):
    s = input()
    if s[1] == "+":
        answer += 1
    else:
        answer -= 1
print(answer)
