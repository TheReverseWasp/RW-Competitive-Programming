from statistics import median 
from copy import copy

n = int(input())

p = list(map(int, input().split()))

m = median(p)

memory = dict()

def register_hotel(prev, next_):
    if prev >= 0 and next_ < n:
        if not (prev, next_) in memory:
            med = median(p[prev:next_ + 1])
            memory[(prev, next_)] = med
            return memory[(prev, next_)]
        else:
            return memory[(prev, next_)]
    else:
        return -1
def grow(prev, next_, val):
    if prev >= 0 and next_ < n:
        t0 = register_hotel(prev, next_)
        t1 = register_hotel(prev, next_+2,)
        t2 = register_hotel(prev-2, next_)
        t3 = register_hotel(prev-1, next_+1)
        temp_list = list([t0, t1, t2, t3])
        temp_list_2 = list([next_ - prev + 1, next_ - prev + 1 + 2, next_ - prev + 1 + 2, next_ - prev + 1 + 2])
        
        min_range = 999999999
        for med, ans_val in zip(temp_list, temp_list_2):
            if med != -1 and med != val and ans_val < min_range and ans_val != -1:
                min_range = ans_val
        if min_range == 999999999:
            t_1 = grow(prev, next_+2, val) #right
            t_2 = grow(prev-2, next_, val) #left
            t_3 = grow(prev-1, next_+1, val) #mid
            min_range = 999999999
            for elem in [t_1, t_2, t_3]:
                if elem != -1 and elem < min_range:
                    min_range = elem
            if min_range == 999999999:
                return -1
        return min_range
    else:
        return -1
for i in range(n):
    prev = copy(i)
    next_ = copy(i)
    ans = grow(prev, next_, p[i])
    print(ans, end = " ")
print()
