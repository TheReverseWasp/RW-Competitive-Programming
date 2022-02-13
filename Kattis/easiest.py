tc = input()
while tc != "0":
    sum_ = sum(list(map(int, [c for c in tc])))
    temp = int(tc)
    for i in range(11, 101):
        t = str(temp * i)
        if sum_ == sum(list(map(int, [c for c in t]))):
            print(i)
            break
    tc = input()
