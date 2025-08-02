s = input()
db = [-1 for i in range(110)]

def find_all(acum, pos):
    ans = 0
    if acum == "QAQ":
        return 1
    if pos == len(s):
        return 0
    if acum == "QA":
        if s[pos] == "Q":
            acum = "QAQ"
            ans = ans + find_all(acum, pos + 1)
            acum = "QA"
            ans = ans + find_all(acum, pos + 1)
        else:
            ans = ans + find_all(acum, pos + 1)
    elif acum == "Q":
        if s[pos] == "A":
            acum = "QA"
            ans = ans + find_all(acum, pos + 1)
            acum = "Q"
            ans = ans + find_all(acum, pos + 1)
        else:
            ans = ans + find_all(acum, pos + 1)
    else:
        if s[pos] == "Q":
            acum = "Q"
            ans = ans + find_all(acum, pos + 1)
            acum = ""
            ans = ans + find_all(acum, pos + 1)
        else:
            ans = ans + find_all(acum, pos + 1)
    return ans


print(find_all("", 0))

