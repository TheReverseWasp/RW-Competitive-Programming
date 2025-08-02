table_c = input()
hand = list(input().split())
play = False
for elem in hand:
    if table_c[0] == elem[0] or table_c[1] == elem[1]:
        play = True
        break
print("YES" if play else "NO")