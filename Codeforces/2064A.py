tc = int(input())
for _ in range(tc):
    n = int(input())
    s = input()
    search_for = 1
    ans = 0 
    for elem in s:
        if elem == str(search_for):
            ans += 1
            search_for += 1
            search_for %= 2

    print(ans)