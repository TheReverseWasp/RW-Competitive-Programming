def comb_rep(n):
    return n*n

t = int(input())
while t:
    t-=1
    n = int(input())
    s = input()
    zeros, ones = 0, 0
    for char in s:
        if char == "0":
            zeros += 1
        else:
            ones += 1
    print(zeros, ones)
    print(comb_rep(zeros)+comb_rep(ones))
