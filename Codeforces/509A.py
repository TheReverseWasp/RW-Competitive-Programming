from copy import copy

n = int(input())
prev_row = [1 for i in range(n)]
curr_len = 1
while curr_len < n:
    new_row = [1]
    while len(new_row) < n:
        new_row.append(new_row[-1] + prev_row[len(new_row)])
    prev_row = copy(new_row)
    curr_len += 1
print(prev_row[-1])