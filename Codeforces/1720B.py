for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    maxo, mini = max(a), min(a)
    maxo_pos = -1
    mini_pos = -1
    for idx, elem in enumerate(a):
        if elem == maxo:
            maxo_pos = idx+0
        if elem == mini:
            mini_pos = idx+0

    a = a[:min(maxo_pos, mini_pos)] + a[min(maxo_pos, mini_pos)+1:max(maxo_pos, mini_pos)] + a[max(maxo_pos, mini_pos)+1:]
    print(maxo - mini + max(a) - min(a))