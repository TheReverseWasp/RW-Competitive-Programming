tc = int(input())
for __ in range(tc):
    n = int(input())
    s = input()
    ini, fin = -1, -1
    for i in range(n):
        if s[i] == "B":
            if ini == -1:
                ini = i + 0
            fin = i + 0
    print(fin - ini +1)