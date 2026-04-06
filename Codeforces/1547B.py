tc = int(input())
temp = "abcdefghijklmnopqrstuvwxyz"
for _ in range(tc):
    s = input()
    runner = ""
    for elem in temp:
        if len(runner) == len(s):
            break
        way_1 = runner + elem
        way_2 = elem + runner
        if way_1 in s:
            runner = way_1 + ""
            continue
        elif way_2 in s:
            runner = way_2 + ""
            continue
        else:
            break
    if runner != s:
        print("NO")
    else:
        print("YES")