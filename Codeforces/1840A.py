tc = int(input())
for __ in range(tc):
    n = int(input())
    a = input()
    ans = ""
    while len(a) > 0:
        ans+= a[0]
        returner = a[1:].find(a[0])
        a = a[returner+2:]
    print(ans)