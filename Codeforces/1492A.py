tc = int(input())
for _ in range(tc):
    p,a,b,c = map(int,input().split())
    if p % a == 0 or p % b == 0 or p % c == 0:
        print(0)
        continue
    print(min([
        ((p//a) + 1)*a - p,
        ((p//b) + 1)*b - p,
        ((p//c) + 1)*c - p,
    ]))