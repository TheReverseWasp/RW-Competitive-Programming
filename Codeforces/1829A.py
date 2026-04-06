comp = "codeforces"
tc = int(input())
for __ in range(tc):
    s = input()
    ans = 0
    for i in range(len(comp)):
        if comp[i] != s[i]:
            ans+=1
    print(ans)