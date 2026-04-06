tc = int(input())
for i in range(tc):
    victim = list(map(int,input().split()))
    victim.sort()
    print(victim[1])