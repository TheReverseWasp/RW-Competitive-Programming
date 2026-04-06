n = int(input())
a = list(map(int,input().split()))
a_lol = [abs(elem) for elem in a]
print(min(a_lol))