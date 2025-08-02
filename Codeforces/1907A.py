tc = int(input())
for __ in range(tc):
    pos = input()
    let, num = "abcdefgh", "12345678"
    s = set()
    for num_runner in num:
        s.add(pos[0] + num_runner)
    for let_runner in let:
        s.add(let_runner + pos[1])
    for elem in s:
        if elem == pos:
            continue
        print(elem)