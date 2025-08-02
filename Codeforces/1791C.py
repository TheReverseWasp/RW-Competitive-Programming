tc = int(input())
for __ in range(tc):
    n = int(input())
    s = input()
    ini = 0
    fin = n - 1
    while ini < fin:
        if s[ini] != s[fin]:
            n -= 2
            ini += 1
            fin -= 1
        else:
            break
    print(n)
