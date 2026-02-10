tc=int(input())
for _ in range(tc):
    n,m=map(int,input().split())
    bottom = set(list(map(int,input().split())))
    left = set(list(map(int,input().split())))
    print(len(bottom.intersection(left)))