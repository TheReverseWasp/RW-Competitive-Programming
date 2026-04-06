tc = int(input())
for _ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    negative, positive = 0, 0
    for elem in a:
        if elem < 0:
            negative += elem
        else:
            positive += elem
    negative = abs(negative)
    print(max(negative, positive) - min(negative, positive))