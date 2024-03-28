from copy import copy

def is_lower(elem1, elem2):
    if len(elem1) < len(elem2):
        return True
    if len(elem1) == len(elem2):
        return elem1 <= elem2
    else:
        return False
    
def decompose(s):
    ans = [c for c in s]
    return ans

def is_sorted(elems):
    for i in range(len(elems) - 1):
        if not is_lower(elems[i], elems[i + 1]):
            return False
    return True

def is_possible(elems):
    i = 0
    has_descompose = False
    while i < len(elems) - 1:
        if is_lower(elems[i], elems[i + 1]):
            i += 1
            pass
        else:
            if len(elems[i]) == 1:
                return "NO"
            else:
                has_descompose = True
                temp = list()
                for elem in elems[:i]:
                    temp.append(elem)
                for elem in decompose(elems[i]):
                    temp.append(elem)
                for elem in elems[i+1:]:
                    temp.append(elem)
                elems = temp                  
    if is_sorted(elems):
        return "YES"
    else:
        if has_descompose:
            return is_possible(elems)
        return "NO"


t = int(input())
while t:
    t-=1
    n = int(input())
    a = input()
    a = list(a.split())

    print(is_possible(a))