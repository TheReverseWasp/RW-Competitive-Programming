from copy import copy

def longest_0s(s):
    max_count = 0
    temp = 0
    i = 0
    first_change = -1
    last_change = -1
    had_bridge = False
    while i < len(s):
        if s[i] == '1':
            if first_change == -1:
                first_change = copy(i)
            else:
                if had_bridge and last_change == -1:
                    last_change = copy(i)
                elif last_change != -1:
                    temp = i - first_change + 1
                    if temp > max_count:
                        max_count = copy(temp)
            i += 1
        else:
            if first_change == -1:
                first_change = copy(i)
            if had_bridge == False:
                had_bridge = True
                i += 1
            elif last_change == -1:
                i += 1
            else:
                temp = i - first_change
                if temp > max_count:
                    max_count = copy(temp)
                i = copy(last_change)
                first_change = copy(last_change)
                last_change = -1
                had_bridge = False
    if max_count == 0:
        return len(s)
    if first_change != -1:
        temp = i - first_change 
        if temp > max_count:
            return temp
    return max_count

t = int(input())
while t:
    t-=1
    n = int(input())
    s = input()
    s = [c for c in s]
    max_count = longest_0s(s)
    print(max_count)