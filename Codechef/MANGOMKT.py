from operator import itemgetter

def set_query(val, d):
    visited = set()
    answer = 0
    while len(visited) < len(val):
        l = []
        for key in d.keys():
            if not key in visited:
                l.append([key,len(d[key]) * val[key - 1]])
        k = sorted(l, key=itemgetter(1))
        selected_key = l[0][0]
        visited.add(selected_key)
        answer += val[selected_key - 1]
        for i in range(len(val)):
            if i != selected_key - 1:
                if i + 1 in d[selected_key]:
                    val[i] += 1
                else:
                    val[i] -= 1
    return val, answer

n,q = map(int,input().split())

val = list(map(int,input().split()))
d = {}
for i in range(q):
    temp1, temp2 = map(int,input().split())
    if not temp1 in d:
        d[temp1] = set()
    if not temp2 in d:
        d[temp2] = set()
    d[temp1].add(temp2)
    d[temp2].add(temp1)
q = int(input())
while q:
    q-=1
    q_string = input()
    if q_string[0] == "+":
        q_string = q_string[2:]
        temp1, temp2 = map(int,q_string.split())
        if not temp1 in d:
            d[temp1] = set()
        if not temp2 in d:
            d[temp2] = set()
        d[temp1].add(temp2)
        d[temp2].add(temp1)
    elif q_string[0] == "-":
        q_string = q_string[2:]
        temp1, temp2 = map(int,q_string.split())
        if not temp1 in d:
            d[temp1] = set()
        if not temp2 in d:
            d[temp2] = set()
        d[temp1].remove(temp2)
        d[temp2].remove(temp1)
    else:
        val, answer = set_query(val, d)
        print(answer)
