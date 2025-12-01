tc = int(input())
for __ in range(tc):
    a,b,k = map(int,input().split())
    evens = k // 2
    odds = k % 2
    even_leap = a - b
    odd_leap = a
    print(even_leap*evens+odds*odd_leap)