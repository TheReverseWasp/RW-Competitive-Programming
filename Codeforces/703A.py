n = int(input())
mishka = 0
chris = 0
for __ in range(n):
    m, c = map(int,input().split())
    if m > c:
        mishka += 1
    elif m == c:
        continue
    else:
        chris += 1

if mishka > chris:
    print("Mishka")
elif mishka < chris:
    print("Chris")
else:
    print("Friendship is magic!^^")