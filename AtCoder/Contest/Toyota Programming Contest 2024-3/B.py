
from copy import copy
temp = input()
ans = list()
while(temp != '0'):
    ans.append(copy(temp))
    temp = input()
ans.append("0")
for i in range(-1, -len(ans) - 1, -1):
    print(ans[i])