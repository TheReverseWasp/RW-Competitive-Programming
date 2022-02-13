import copy as cp

[n, t] = list(map(int, input().split()))
cad = input()
bp =[]
for i in range(len(cad)):
    if cad[i] == "B":
        bp.append(i)
bp.reverse()
nl = cp.copy(bp)
for i in range(t):
    for j in range(len(bp)):
        if j == 0:
            if bp[j] < n - 1:
                nl[j] = bp[j] + 1 
        else:
            if bp[j] != bp[j - 1] - 1:
                nl[j] = bp[j] + 1
            else:
                nl[j] = bp[j]
    bp = cp.copy(nl)
bp.reverse()
bp.append(10000)
it = 0
pos = 0
while it < n:
    if it != bp[pos]:
        print("G", end="")
    else:
        print("B", end="")
        pos += 1
    it += 1
print()