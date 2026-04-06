tc = int(input())
for _ in range(tc):
    n, s = map(int,input().split())
    to_search = n + 0
    n += 1
    to_search = to_search*to_search
    possible = s // to_search        
    if possible > n:
        print(n - 1)
    else:
        print(possible)