tc = int(input())
for _ in range(tc):
    a = [letter for letter in input()]
    a.sort(reverse=True)
    print("".join(a))