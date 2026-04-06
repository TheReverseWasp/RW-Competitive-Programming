tc = int(input())
runner = "Yes"
for __ in range(tc):
    s = input()
    ini_pos = 0
    if s[0] == "e":
        ini_pos = 1
    elif s[0] == "s":
        ini_pos = 2
    else:
        pass
    flag = True
    for i in range(len(s)):
        if s[i] != runner[ini_pos]:
            flag = False
            break
        ini_pos += 1
        ini_pos %=3
    if flag:
        print("YES")
    else:
        print("NO")