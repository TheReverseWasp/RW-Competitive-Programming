b, f = map(int, input().split())
while b != 0 or f != 0:
    if b + f == 13:
        print("Never speak again.")
    elif b > f:
        print("To the convention.")
    elif f > b:
        print("Left beehind.")
    else: 
        print("Undecided.")
    b, f = map(int, input().split())
