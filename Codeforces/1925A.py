tc=int(input())
dic="abcdefghijklmnopqrstuvwxyz"
for __ in range(tc):
    n,k=map(int,input().split())
    print(n*dic[:k])
