f, bh = map(int, input().split())
fhl = list(map(int, input().split()))
####
for i in range(len(fhl)):
    if fhl[i] > bh:
        f += 1
print(f)
