tc = int(input())
for __ in range(tc):
    keyboard = input()
    word = input()
    current_pos = keyboard.find(word[0])
    ans = 0
    for i in range(1,len(word)):
        new_pos = keyboard.find(word[i])
        ans += abs(new_pos - current_pos)
        current_pos = new_pos + 0
    print(ans)