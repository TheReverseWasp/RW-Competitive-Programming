tc = int(input())
for _ in range(tc):
    n,k = map(int,input().split())
    b = list(map(int,input().split()))
    actual = 1
    for elem in b:
        actual *= elem
    if 2023 % actual != 0:
        print("no")
        continue
    else:
        print("yes")
    ans = list()
    ans.append(2023//actual)
    while len(ans) < k:
        ans.append(1)
    print(" ".join([str(num) for num in ans]))