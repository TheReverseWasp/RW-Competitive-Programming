tc = int(input())

for __ in range(tc):
    line = list(input().split())
    for word in line:
        print(word[0], end="")
    print()