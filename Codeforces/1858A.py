tc = int(input())
for __ in range(tc):
    a,b,c = map(int, input().split())
    a_tricks = c // 2 + c % 2
    b_tricks = c - a_tricks
    if a + a_tricks > b + b_tricks:
        print("First")
    else:
        print("Second")