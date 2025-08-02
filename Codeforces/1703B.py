tc = int(input())
for __ in range(tc):
    n = int(input())
    s = input()
    seto = set()
    ans = 0
    for letter in s:
        if letter in seto:
            ans += 1
        else:
            seto.add(letter)
            ans += 2
    print(ans)
