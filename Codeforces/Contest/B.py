t = int(input())
while t:
    t-=1
    p, m = map(int, input().split())
    teams = 0
    if m != 0 and p != 0 and max(p,m) >= min(p,m) + 2:
        if p > m:
            teams += min(int((p-m)  / 2), m)
            p -= teams * 3
            m -= teams
        else:
            teams += min(int((m-p) / 2), p)
            p -= teams
            m -= teams * 3
    teams += int(min(p,m)/2)
    p -= teams * 2
    m -= teams * 2
    if (p == 1 and m >= 3) or (m == 1 and p >= 3):
        teams += 1
    print(teams)
