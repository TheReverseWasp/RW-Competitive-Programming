temp = "codeforces"
dic = set([letter for letter in temp])
tc = int(input())
for i in range(tc):
    letter_tt = input()
    print("YES" if letter_tt in dic else "NO")