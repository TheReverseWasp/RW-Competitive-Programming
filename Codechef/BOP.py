t = int(input())
while t:
    t-=1
    n,m,q = map(int, input().split())
    s = input()
    s = [1 if s[i] == "1" else 0 for i in range(len(s))]
    while q:
        q-=1
        q_s = input()
        s = [1 if q_s == "1" else 0] + s
        ans = 0
        temp = 0
        prev_mod = []
        for i in range(len(s) - m + 1):
            if (s[i] + temp) % 2 == 1:
                ans += 1
                prev_mod.append(1)
            else:
                prev_mod.append(0)
            temp = sum(prev_mod[-m + 1:])
        print(ans)
