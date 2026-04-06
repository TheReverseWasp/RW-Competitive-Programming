dic = "abcdefghijklmnopqrstuvwxyz"
w = input()
st = 0
ans = 0
for letter in w:
    pos = dic.find(letter)
    abo = abs(st - pos)
    neg_abo = len(dic) - abo
    st = pos + 0
    ans += min(abo, neg_abo)
print(ans)
