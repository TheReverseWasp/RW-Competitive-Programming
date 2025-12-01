tc = int(input())
for __ in range(tc):
    alice, bob = 0,0
    a = list(map(int,input().split()))
    a.sort()
    alice = a[0] + 0
    bob = a[1] + 0
    a[-1] -= bob - alice
    alice = bob + 0
    alice += a[-1] // 2
    bob += a[-1] - (a[-1] // 2)
    if alice == bob:
        print(alice)
    else:
        print(min(alice, bob))
