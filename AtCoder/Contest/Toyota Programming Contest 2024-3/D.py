t = input()
bags = int(input())
bags_strings = list()
while bags:
    bags -= 1
    bags_strings.append(list(input().split()))
    bags_strings[-1].append('')
ans = set()
def recursive_bags(bags_strings, acum_string, acum_cost, starting_point):
    if acum_string == t:
        ans.add(acum_cost)
        return
    if len(acum_string) > len(t):
        return
    if len(acum_string) == len(t) and acum_string != t:
        return
    for i in range(starting_point, len(bags_strings)):
        for elem in bags_strings[i]:
            if elem != '':
                temp = acum_string + elem
                recursive_bags(bags_strings, temp, acum_cost + 1, starting_point + 1)
            else:
                recursive_bags(bags_strings, acum_string, acum_cost, starting_point + 1)
    ans.add(-1)

recursive_bags(bags_strings, '', 0, 0)
ans = list(ans)
ans.sort()
if len(ans) > 1:
    print(ans[1])
else:
    print(ans[0])