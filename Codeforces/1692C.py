tc = int(input())
db_h = ["" for i in range(8)]
for __ in range(tc):
    input()
    for i in range(8):
        db_h[i] = input()
    ans = []
    for i in range(8):
        if "#.#" in db_h[i]:
            x = db_h[i].find("#.#") + 2
            y = i + 2
            ans = [str(y), str(x)]
            break
    print(" ".join(ans))