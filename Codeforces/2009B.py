tc = int(input())
for __ in range(tc):
    steps = int(input())
    ans = list()
    for __ in range(steps):
        temp = input()
        ans.append(str(temp.find("#") + 1))
    ans = ans[::-1]
    print(" ".join(ans))