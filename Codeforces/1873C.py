db = {
    (4,4):5,
    (5,4):5,
    (4,5):5,
    (5,5):5,
}
def is_valid(play):
    return play[0] > -1 and play[0] < 10 and play[1] > -1 and play[1] < 10

queue = list(db.keys())
movements = [(0,1),(0,-1),(-1,0),(0,-1),(-1,1),(1,-1),(-1,-1),(1,1)]
i = 0
while i < len(queue):
    for mov in movements:
        play = (queue[i][0] + mov[0], queue[i][1] + mov[1])
        if is_valid(play) and not play in db:
            db[play] = db[queue[i]] - 1
            queue.append(play)
    i+=1

answer = list([0 for i in range(10)] for i in range(10))
for pos, val in db.items():
    answer[pos[0]][pos[1]] = val

#for elem in answer:
#    print(elem)
    

tc = int(input())
for __ in range(tc):
    answer = 0
    for x in range(10):
        line = input()
        for y in range(10):
            if line[y] == "X":
                answer += db[(x,y)]
    print(answer)