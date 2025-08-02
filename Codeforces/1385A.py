tc = int(input())
for __ in range(tc):
    elems = list(map(int,input().split()))
    max_elem = max(elems)
    count_max = elems.count(max_elem)
    if count_max >= 2:
        print("YES")
        print(max_elem, min(elems), min(elems))
    else:
        print("NO")