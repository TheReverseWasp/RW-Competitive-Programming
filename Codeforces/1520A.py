tc = int(input())
for __ in range(tc):
    n = int(input())
    s = input()
    re_s = "0"
    i = 0
    while i < n:
        if s[i] == re_s[-1]:
            i += 1
            continue
        re_s += s[i]
        i+=1
    ans = True
    for j in range(len(re_s)):
        if re_s[j] in re_s[j + 1:]:
            ans = False
            break
    if ans:
        print("YES")
    else:
        print("NO")
