vowels = "aeiouy"
s = input().lower()
answer = ""
for i in s:
    if vowels.find(i) == -1:
        answer += "." + i
print(answer)