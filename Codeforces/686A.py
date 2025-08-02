kids, x = map(int,input().split())
d = 0
for __ in range(kids):
    sign, amount = input().split()
    amount = int(amount)
    if sign == "+":
        x += amount
    else:
        if amount > x:
            d += 1
        else:
            x-=amount
print(x, d)