tc = int(input())
for __ in range(tc):
    m,a,b,c = map(int, input().split())
    ra,rb = m + 0, m + 0 
    ans = 0
    ###
    sit_a = min(a,ra)
    ans+=sit_a
    ra-=sit_a
    ###
    sit_b = min(b,rb)
    ans+=sit_b
    rb-=sit_b
    ###
    sit_any = min(c,ra+rb)
    ans += sit_any
    ###
    print(ans)