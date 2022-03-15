t = int(input())
while t:
    t-=1
    a,b = map(int, input().split())
    even_a, even_b = int(a/2), int(b/2)
    odd_a, odd_b = a-even_a, b-even_b
    print(even_a *even_b + odd_a * odd_b)
