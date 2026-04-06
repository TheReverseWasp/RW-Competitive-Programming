t = int(input())
while t:
    t-=1
    n, a, b = map(int, input().split())
    l = list(map(int, input().split()))
    both, alice, bob = 0,0,0
    for elem in l:
        if elem % a == 0 and elem % b == 0:
            both += 1
        elif elem % a == 0:
            bob += 1
        elif elem % b == 0:
            alice += 1

    if both > 1:
        bob += 1
    if bob > alice:
        print("BOB")
    else:
        print("ALICE")
