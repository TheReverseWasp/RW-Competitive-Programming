
def calc_cost(row, d):
    memory = list()
    for i in range(len(row)):
        memory.append(1000000000)
    memory[-1] = row[-1] + 1
    for i in range(-2, -len(row) - 1, -1):
        if i + d + 2 >= 0:
            memory[i] = row[i] + 1 + min(memory[i + 1:])
        else:
            memory[i] = row[i] + 1 + min(memory[i + 1: i + d + 2])
    return memory[0]

t = int(input())
while t:
    t-=1
    n, m, k, d = map(int,input().split())
    deepness = list()
    for i in range(n):
        deepness.append(list(map(int,input().split())))
    cost_list = list()
    for row in deepness:
        cost_list.append(calc_cost(row, d))
    consecutive_max_cost = 10000000000000000
    for i in range(len(cost_list) - k + 1):
        temp = sum(cost_list[i: i + k])
        if temp < consecutive_max_cost:
            consecutive_max_cost = temp
    print(consecutive_max_cost)