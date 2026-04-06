drinks = int(input())
drnk_l = list(map(int, input().split()))

orange_party = sum(drnk_l) / drinks
print("{:.6f}".format(orange_party))