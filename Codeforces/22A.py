n = int(input())
a = list(map(int,input().split()))
a.sort()
flag = False
for i in range(1,n):
    if a[i] != a[0]:
        flag = True
        print(a[i])
        break
if not flag:
    print("NO")