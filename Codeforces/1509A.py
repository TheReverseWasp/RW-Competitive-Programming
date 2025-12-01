tc = int(input())
for _ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    odds, evens = [str(elem) for elem in a if elem % 2 == 1], [str(elem) for elem in a if elem % 2 == 0]
    print(" ".join(odds) + " " + " ".join(evens))