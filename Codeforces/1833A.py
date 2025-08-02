tc = int(input())
for __ in range(tc):
    n = int(input())
    seto = set()
    s = input()
    for i in range(n-1):
        seto.add(s[i:i +2])
    print(len(seto))