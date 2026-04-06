t = int(input())
while t:
    t-=1
    s =input()
    flag = True
    d = {"R":0, "G":0}
    for c in s:
        if not c in d:
            d[c] = 0
        d[c] += 1
    if d["R"] != d["G"]:
        flag = False
    d = {"R":0, "G":0}
    for i in range(len(s)):
        if s[i] == s[(i+1)%len(s)]:
            d[s[i]] += 1

    if d["R"] > 1 or d["G"] > 1:
        flag = False
    
    if flag:
        print("yes")
    else:
        print("no")
    