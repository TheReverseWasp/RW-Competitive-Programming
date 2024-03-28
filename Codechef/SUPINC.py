t = int(input())
while t:
    t-=1
    n, k, elem = map(int, input().split())
    margin = ((k * (k + 1)) // 2) - 1
    if elem > margin:
        print("Yes")
    else:
        print("No")