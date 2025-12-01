dump = "abcdefghijklmnopqrstuvwxyz"

dic = {letter:pos for letter, pos in zip(dump, range(len(dump)))}

def calc_diff(a,b):
    ans = 0
    for i in range(len(a)):
        ans += abs(dic[a[i]] - dic[b[i]])
    return ans

tc = int(input())
for __ in range(tc):
    n,m = map(int,input().split())
    word_list = list()
    for i in range(n):
        word_list.append(input())
    ans = -1
    for i in range(n):
        for j in range(i+1,n):
            diff = calc_diff(word_list[i], word_list[j])
            if ans == -1 or diff < ans:
                ans = diff + 0
    print(ans)
    