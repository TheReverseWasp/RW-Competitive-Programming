temp = 1
running_list = [0]
while temp < 500000:
    running_list.append(temp + 0)
    temp *= 2

def quality_assurace(temp_a,temp_b,temp_c):
    a = temp_a + 0
    b = temp_b + 0
    c = temp_c + 0
    left_nodes = 0
    for i in range(len(running_list)):
        if a >= running_list[i]:
            a-=running_list[i]
            left_nodes = running_list[i + 1]
        else:
            left_nodes += a
            break
    if c != left_nodes:
        return -1
    height = i 
    if a != 0:
        if left_nodes - (2 * a) >= b:
            b -= left_nodes - (2 * a)
        height += 1  
    height += b // left_nodes
    if b % left_nodes != 0:
        height += 1
    height -= 1
    return height
    

t = int(input())
while t:
    t-=1
    a,b,c = map(int,input().split())
    height = quality_assurace(a,b,c)
    print(height)