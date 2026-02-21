for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    diffs = []
    for idx, elem in enumerate(a):
        diffs.append(elem - idx - 1)
    print(max(0, max(diffs)))