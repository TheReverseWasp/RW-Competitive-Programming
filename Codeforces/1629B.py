tc = int(input())
for _ in range(tc):
    l,r,k = map(int,input().split())
    if r-l == 0 and l != 1:
        print("YES")
        continue
    elif r-l == 0 and l == 1:
        print("NO")
        continue
    terms = r-l+1
    if l % 2 == 1:
        terms +=1
    odds = terms // 2
    if odds <= k:
        print("YES")
    else:
        print("NO")
    