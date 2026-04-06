tc = int(input())
for _ in range(tc):
    s = input()
    if s.find("1") < s.find("3"):
        print(13)
    else:
        print(31)