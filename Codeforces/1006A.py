n = int(input())
a = list(map(int,input().split()))
ans = []
for elem in a:
    if elem % 2 == 0:
        ans.append(str(elem-1))
    else:
        ans.append(str(elem))
print(" ".join(ans))
