db = {}
dic = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(dic)):
    eq = str(i + 1)
    if len(eq) == 2:
        eq += "0"
    db[eq] = dic[i]

tc = int(input())
for __ in range(tc):
    n = int(input())
    s = input()
    i = -1
    ans = ""
    while len(s) > 0:
        if s[i] == "0":
            i-=2
        else:
            i-=0
        ans += db[s[i:]]
        s = s[:i]
        i=-1
    print(ans[::-1])