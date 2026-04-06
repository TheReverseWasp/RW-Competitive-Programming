tc = int(input())
for __ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    b = sorted(a)
    max_diff = b[-1] - b[-2] 
    max_item = b[-1]
    ans = list()
    for elem in a:
        if elem == max_item:
            ans.append(max_diff)
        else:
            ans.append(elem - max_item)
    for elem in ans:
        print(elem, end=" ")
    print()