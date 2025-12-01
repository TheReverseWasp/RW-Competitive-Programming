tc = int(input())
for __ in range(tc):
    s = input()
    ones, zeros = s.count("1"), s.count("0")
    mini, maxi = min(zeros, ones), max(zeros, ones)
    if mini == 0:
        print(0)
    elif mini == maxi:
        if mini - 1 > 0:
            print(mini-1)
        else:
            print(0)
    else:
        print(mini)