tc = int(input())
for __ in range(tc):
    arr = list(map(int,input().split()))
    arr.sort()
    print(abs(arr[0]-arr[1])+abs(arr[1]-arr[1])+abs(arr[1]-arr[2]))