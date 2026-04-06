tc = int(input())
while tc:
    prz = int(input())
    games = input()
    c_score = 0
    cf_score = 0
    for i in games:
        if i == "C":
            c_score += 2
        elif i == "D":
            c_score += 1
            cf_score += 1
        else:
            cf_score += 2
    if c_score > cf_score:
        print(60*prz)
    elif c_score < cf_score:
        print(40*prz)
    else:
        print(55*prz)

    tc-=1
