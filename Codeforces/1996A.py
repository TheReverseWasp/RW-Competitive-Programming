tc = int(input())
for __ in range(tc):
    legs = int(input())
    animals = legs // 4
    legs %= 4
    animals += legs // 2
    print(animals)