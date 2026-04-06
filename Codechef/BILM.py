def lex_smaller(t1, t2):
    if t1 == t2[:len(t1)] and len(t1) <= len(t2):
        return True
    if t1 < t2[:len(t1)]:
        return True
    return False
t = int(input())
while t:
    t-=1
    n, q = map(int, input().split())
    s = input()
    while q:
        q-=1
        idx = s.find('1')
        if idx > 0:
            temp1 = s[:idx] + s[idx+1:]
            val = '0'
            temp2 = s[:idx] + val + s[idx+1:]
            if lex_smaller(temp1, temp2):
                to_compare = temp1
            else:
                to_compare = temp2
            if lex_smaller(to_compare, s):
                s = to_compare
            else:
                break
        else:
            s = s[1:]
    print(s)
            