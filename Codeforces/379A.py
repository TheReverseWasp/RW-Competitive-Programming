a,b = map(int,input().split())
ans = a + 0
restos = a + 0
while restos >= b:
    ans += restos // b
    restos = restos % b + restos // b
print(ans)
