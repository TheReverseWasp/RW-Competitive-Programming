tc=int(input())
for _ in range(tc):
    a,b=map(int,input().split())
    s = input() + input()[::-1]
    amsiedad = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            amsiedad += 1
    if amsiedad >= 2:
        print("no")
    else:
        print("yes")