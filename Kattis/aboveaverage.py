from statistics import mean

ex = int(input())
for i in range(ex):
    l = list(map(float, input().split()))
    l = l[1:]
    avg_score = mean(l)
    c = 0
    for i in l:
        if i > avg_score:
            c += 1
    sc = str(round(c/len(l) * 100, 3))
    while sc.find(".") - len(sc) != -4:
        sc += "0"
    print(f"{sc}%")
