tc=int(input())
for _ in range(tc):
    k =  int(input())
    runner = 1
    col, row = 1,1
    while k > 0:
        if k - runner <= 0:
            if k - (runner // 2 + 1) <= 0:
                col = runner // 2 + 1
                row = k + 0
            else:
                col = runner // 2 + 1 - (k - runner//2 - 1)
                row = runner // 2 + 1
            k = 0
        else:
            k -= runner
            runner += 2
    print(row,col)