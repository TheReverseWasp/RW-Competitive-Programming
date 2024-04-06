from copy import copy

n, m = map(int, input().split())

grid = list()
for i in range(n):
    grid.append(input())

medicines = int(input())
med_dict = dict()
for i in range(medicines):
    temp = tuple(map(int, input().split()))
    med_dict[(temp[0], temp[1])] = temp[2]

st_r, st_c = -1, -1
for i in range(n):
    for j in range(m):
        if grid[i][j] == "S":
            st_r = i
            st_c = j
            break
    if st_r != -1:
        break

ans = False
def map_grid(currently, recorrido, med_kit, energy = 1):
    global ans
    if ans:
        return
    if currently[0] >= n or currently[1] >= m:
        return
    if grid[currently[0]][currently[1]] == "#":
        return
    if currently in recorrido:
        return
    new_recorrido = copy(recorrido)
    new_recorrido.add(currently)
    new_energy = energy + 0
    new_med_kit = copy(med_kit)
    if currently in med_kit:
        if energy < med_kit[currently]:
            new_energy = med_kit[currently]
            del new_med_kit[currently]
        else:
            new_energy = energy + 0
    if grid[currently[0]][currently[1]] == "T":
        ans = True
        return
    if new_energy <= 0:
        return
    map_grid((currently[0] + 1, currently[1]), new_recorrido, new_med_kit, energy=new_energy - 1)
    map_grid((currently[0] - 1, currently[1]), new_recorrido, new_med_kit, energy=new_energy - 1)
    map_grid((currently[0], currently[1] + 1), new_recorrido, new_med_kit, energy=new_energy - 1)
    map_grid((currently[0], currently[1] - 1), new_recorrido, new_med_kit, energy=new_energy - 1)

map_grid((st_r, st_c), set(), med_kit=med_dict)
if ans:
    print("Yes")
else:
    print("No")