tc = int(input())
abc = "abcdefghijklmnop"
while tc > 0:
    l = int(input())
    s = input()
    it = 0
    while it < l:
        t = s[it: it+4]
        pos = 0
        if t[0] == "1":
            pos += 8
        if t[1] == "1":
            pos += 4
        if t[2] == "1":
            pos += 2
        if t[3] == "1":
            pos += 1
        print(abc[pos], end="")
        it += 4
    print()
    tc -= 1
