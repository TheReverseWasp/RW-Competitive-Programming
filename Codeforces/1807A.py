tc = int(input())
for i in range(tc):
    a,b,c = map(int,input().split())
    if a + b == c:
        print("+")
    else:
        print("-")